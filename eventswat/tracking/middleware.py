import re
import logging

from core import helper
from actors import actor_ip
from control.models import RecentlySearch
from leads.models import Lead
from leads.search import search as leadsearch
from tracking.models import Visitor, Pageview
from tracking.utils import get_ip_address, update_recently_view_lead
from tracking.settings import (TRACK_AJAX_REQUESTS,
    TRACK_ANONYMOUS_USERS, TRACK_PAGEVIEWS, TRACK_IGNORE_URLS)
from fixido.util import ip_checking

TRACK_IGNORE_URLS = map(lambda x: re.compile(x), TRACK_IGNORE_URLS)
log = logging.getLogger(__file__)

class VisitorTrackingMiddleware(object):
  def process_response(self, request, response):
    # Session framework not installed, nothing to see here..

    if not hasattr(request, 'session'):            
      return response
    # Do not track AJAX requests..
    #if request.is_ajax() and not TRACK_AJAX_REQUESTS:
    #    return response
    
    # If dealing with a non-authenticated user, we still should track the
    # session since if authentication happens, the `session_key` carries
    # over, thus having a more accurate start time of session
    user = getattr(request, 'user', None)

    # Check for anonymous users
    if not user or user.is_anonymous():
      if not TRACK_ANONYMOUS_USERS:
        return response
      user = None
    
    elif not hasattr(user, 'actor'):
      user = None
    
    elif not user.is_staff:
      user = user.actor

    # Force a save to generate a session key if one does not exist
    if not request.session.session_key:
      request.session.save()

    # A Visitor row is unique by session_key
    session_key = request.session.session_key

    try:
      visitor = Visitor.objects.get(pk=session_key)
      # Update the user field if the visitor user is not set. This
      # implies authentication has occured on this request and now
      # the user is object exists. Check using `user_id` to prevent
      # a database hit.
      if user and not visitor.user_id:
        visitor.user = user
    except Visitor.DoesNotExist:
      # Log the ip address. Start time is managed via the
      # field `default` value
      visitor = Visitor(pk=session_key, ip_address=get_ip_address(request),
          user_agent=request.META.get('HTTP_USER_AGENT', None))

    visitor.expiry_age = request.session.get_expiry_age()
    visitor.expiry_time = request.session.get_expiry_date()

    # Be conservative with the determining time on site since simply
    # increasing the session timeout could greatly skew results. This
    # is the only time we can guarantee.
    now = helper.get_now()
    time_on_site = 0
    if visitor.start_time:
      time_on_site = (now - visitor.start_time).seconds
    visitor.time_on_site = time_on_site
    
    ip_number = actor_ip()
    #if not get_ip_address(request).startswith("66.249"):
    if not ip_checking(get_ip_address(request)):
      visitor.save()

    if TRACK_PAGEVIEWS:
      # Match against `path_info` to not include the SCRIPT_NAME..
      path = request.path_info.lstrip('/')
      for url in TRACK_IGNORE_URLS:
        if url.match(path):
          break
      else:
        if  'admin' in request.path or \
            'password_reset' in request.path or \
            'jsi18n' in request.path or \
            '/change-password/' in request.path or \
            '/media/' in request.path or \
            '/show_me_the_money/' in request.path: 
          pass
        else:
          #if not get_ip_address(request).startswith("66.249"):
          if not ip_checking(get_ip_address(request)):
            pageview = Pageview(visitor=visitor, view_time=now, actor=user,
              url=request.get_full_path(), ip_address=get_ip_address(request))
            pageview.save()
          
          system_id = request.COOKIES.get('csrftoken')
          if 'access_secret' in request.GET:
            method = 'api'
          else:  
            method = 'websearch'
          
          query = request.REQUEST.get('q')
          if query or query == '':
            if query != None:
              l_search = leadsearch(query)
              leads_count = l_search.count()
              
              if not user:
                rs = RecentlySearch.objects.filter(
                  activity_view=query, system_id=system_id, method=method)
                
                if rs.count() > 1:
                  rs = rs.order_by('-modified')
                  rs = rs.exclude(id=rs[0].id)
                  rs.delete()
                
                #if not ip_number.startswith("66.249"):
                if not ip_checking(get_ip_address(request)):
                  search_q, created = RecentlySearch.objects.get_or_create(
                  activity_view=query, system_id=system_id, method=method)
                
                  if created:
                    search_q.user = user
                
              else:
                rs = RecentlySearch.objects.filter(
                  activity_view=query, method=method, user=user)
                
                if rs.count() > 1:
                  rs = rs.order_by('-modified')
                  rs = rs.exclude(id=rs[0].id)
                  rs.delete()

                #if not ip_number.startswith("66.249"):
                if not ip_checking(get_ip_address(request)):
                  search_q, created = RecentlySearch.objects.get_or_create(
                  activity_view=query, method=method, user=user)
                
                  if created:
                    search_q.system_id = system_id
              
              
              #if not ip_number.startswith("66.249"):
              if not ip_checking(get_ip_address(request)):
                search_q.ip_number = ip_number
                search_q.modified = now
                search_q.leadscount = leads_count
                search_q.save()    

          lead_id = re.match('.*/leads/([0-9]+)/', request.path)
          if lead_id:
            lead_id = lead_id.group(1)
            if Lead.objects.filter(pk=lead_id).exists():
              lead = Lead.objects.get(pk=lead_id)
              update_recently_view_lead(lead, request,'websearch')
            else:
              print 'Lead is not in our system'
    
    return response
