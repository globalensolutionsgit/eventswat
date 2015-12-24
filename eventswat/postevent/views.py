from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from haystack.query import SearchQuerySet
from django.db.models import Q
from datetime import datetime, timedelta


def getevents_by_date(request):
	results = []
	print "request.GET.get('date')", request.GET.get('date')
	print "datetime(datetime.now().date()", datetime.now().date()
	if request.GET.get('date'):
		filter_data = SearchQuerySet().filter(Q(event_startdate_time=request.GET.get('date'))|
								   Q(event_enddate_time=request.GET.get('date')))								    
	else:
		filter_data = SearchQuerySet().filter(Q(event_startdate_time=str(datetime.now().date()))|
								   Q(event_enddate_time=str(datetime.now().date()))) 								  
	for filter_datas in filter_data:
		data = {'id':filter_datas.id.split('.')[-1],'title':filter_datas.eventtitle}
		results.append(data)
		
	return HttpResponse(simplejson.dumps(results), mimetype='application/json')