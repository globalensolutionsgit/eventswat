from django import template
from django.db.models import *
from postbanner.models import *
from events.views import *
from events.models import *
from postevent.models import Postevent
from postbanner.models import PostBanner, BannerPlan
from eventswat.util import *
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
def get_banner(banner):
	banner=PostBanner.objects.all()
	return banner
	
@register.filter
def get_categories(initial_load):  
	category=EventsCategory.objects.all().order_by('id')	
	return category

@register.filter
def get_subcategories(categoryId):  	
	print "get_subcategories"
	subcategories = EventsSubCategory.objects.filter(category__id=categoryId)		
	print "subcategories", subcategories
	return subcategories	

@register.filter
def get_photos(photo): 
	photo=str(photo).split(',')
	return photo[0]

@register.filter
@stringfilter
def get_subcategoriesCount(subCategoryId, categoryId):
	subcategoriescounts = Postevent.objects.filter(event_category_id=categoryId,event_subcategory_id=subCategoryId, admin_status=1).count()
	return subcategoriescounts

# For Adding Events to Google Calendar
@register.filter
def google_calendarize(event):
	from django.contrib.sites.models import Site
	from django.utils.http import urlquote_plus
	st = event.event_startdate_time
	en = event.event_enddate_time and event.event_enddate_time or event.event_startdate_time
	tfmt = '%Y%m%dT000000'

	dates = '%s%s%s' % (st.strftime(tfmt), '%2F', en.strftime(tfmt))
	name = urlquote_plus(event.event_title)
	description = event.event_description

	s = ('http://www.google.com/calendar/event?action=TEMPLATE&' +
		 'text=' + name + '&' +
		 'dates=' + dates + '&' +
		 'details=' + description + '&' +
		 # 'sprop=website:' + urlquote_plus(Site.objects.get_current().domain))
		 'sprop=website:' + urlquote_plus('192.168.1.42:8000'))

	if event.venue:
	    s = s + '&location=' + urlquote_plus(event.venue)

	return s + '&trp=false'
google_calendarize.safe = True
