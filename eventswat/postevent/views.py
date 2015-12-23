from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from postevent.models import (Postevent, PosteventPoster,
                              Organizer, PostEventKeyword)
from events.extra import JSONResponse
from events.models import EventsCategory, EventsSubCategory, City
try:
    import json
except ImportError:
    from django.utils import simplejson as json


@csrf_exempt
def admin_subcategory(request):
    """This function definition for admin postevent add page.
    Using dependent select boxes.SUbcategory load based on category"""
    if request.is_ajax():
        events = EventsSubCategory.objects.filter(
            category__id=request.GET.get('id'))
        return JSONResponse(
            [{'name': obj.subcategory_name, 'id': obj.id, } for obj in events])


@csrf_exempt
def load_country(request):
    """This function definition for load state list based
    on country in forndend postevent page"""
    if request.is_ajax():
        from collections import OrderedDict
        results = []
        unsort_dict = {}
        country = list(
            set(City.objects.values_list('country_name', flat=True)))
        for countries in country:
            unsort_dict[countries] = {'label': countries, 'value': countries}
        sorted_dic = OrderedDict(
            sorted(unsort_dict.iteritems(), key=lambda v: v[0]))
        for k, v in sorted_dic.iteritems():
            results.append(v)
        print 'dsfsadfasfsadf', results
        return HttpResponse(json.dumps(results), mimetype='application/json')


@csrf_exempt
def load_state(request):
    """This function definition for load state
        list based on country in forndend postevent page"""
    if request.is_ajax():
        from collections import OrderedDict
        results = []
        unsort_dict = {}
        state = list(set(
            City.objects.filter(country_name__icontains=request.GET.get(
                'country')).values_list('state', flat=True)))
        for states in state:
            unsort_dict[states] = {'label': states, 'value': states}
        sorted_dic = OrderedDict(
            sorted(unsort_dict.iteritems(), key=lambda v: v[0]))
        for k, v in sorted_dic.iteritems():
            results.append(v)
        return HttpResponse(json.dumps(results), mimetype='application/json')


@csrf_exempt
def load_city(request):
    """This function definition for load state list based
        on country in forndend postevent page"""
    if request.is_ajax():
        from collections import OrderedDict
        results = []
        unsort_dict = {}
        city = list(set(City.objects.filter(
            state__icontains=request.GET.get('state')).values_list(
            'city', flat=True)))
        for cities in city:
            unsort_dict[cities] = {'label': cities, 'value': cities}
        sorted_dic = OrderedDict(
            sorted(unsort_dict.iteritems(), key=lambda v: v[0]))
        for k, v in sorted_dic.iteritems():
            results.append(v)
        return HttpResponse(json.dumps(results), mimetype='application/json')


def postevent(request):
    """Save postevent details,organizer information,poster and
       keywords of postevent"""
    if request.method == 'POST':
        # event details save
        event = Postevent()
        user = Userprofile.objects.get(email=request.user.email)
        event.event_type = request.POST.get('event_type', 'free')
        event.event_category_id = request.POST.get('event_category')
        event.event_subcategory_id = request.POST.get('event_subcategory')
        event.event_title = request.POST.get('event_title')
        event.event_description = request.POST.get('event_desc')
        event.event_startdate_time = request.POST.get('start_date')
        event.event_enddate_time = request.POST.get('end_date')
        event.terms_and_condition = request.POST.get('term_and_cond')
        event.event_website = request.POST.get('url')
        event.is_webinar = request.POST.get('is_webniar')
        event.venue = request.POST.get('venue')
        event.country = request.POST.get('country')
        event.state = request.POST.get('state')
        event.city = request.POST.get('city')
        event.user_name = request.user.username
        event.user_email = request.user.email
        event.user_mobile = user.mobile
        event.save()
        # organizer save
        organizer = Organizer()
        organizer.postevent = event
        organizer.organizer_name = request.POST.get('org_name')
        organizer.organizer_mobile = request.POST.get('org_mobile')
        organizer.organizer_email = request.POST.get('org_email')
        organizer.save()
        # poster image save
        poster_imager = request.FILES.getlist('files[]')
        for post in poster_imager:
            poster = PosteventPoster()
            poster.postevent = event
            poster.event_poster = post
            poster.save()
        # keyword save
        keywords = request.POST.get('keywords')
        trimmed_keyword = keywords.replace(" ", "")
        split_keyword = trimmed_keyword.split(',')
        for keys in split_keyword:
            if keys:
                keyword = PostEventKeyword()
                keyword.keyword = keys
                keyword.save()
                keyword.postevent.add(Postevent.objects.order_by('-pk')[0])
        # redirect page
        category = EventsCategory.objects.all()
        country = City.objects.all()
        country_list = set([countries.country_name.lower()
                            for countries in country])
        context = {'success': 'Your event successfull submitted. \
                               Admin will approved as soon as possible',
                   'category': category, 'country_list': country_list}
    else:
        category = EventsCategory.objects.all()
        country = City.objects.all()
        country_list = set([countries.country_name.lower()
                            for countries in country])
        context = {'category': category, 'country_list': country_list}
    return render_to_response(
        "test.html", context, context_instance=RequestContext(request))
