from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from haystack.query import SearchQuerySet
from django.db.models import Q
from datetime import datetime, timedelta
from models import Postevent


def getevents_by_date(request):
	results = []
	if request.GET.get('date'):
		# filter_data = SearchQuerySet().filter(Q(event_startdate_time=request.GET.get('date'))|
		# 						   Q(event_enddate_time=request.GET.get('date')))

		filter_data = Postevent.objects.filter(Q(event_startdate_time=request.GET.get('date'))|
								   Q(event_enddate_time=request.GET.get('date')))								    								    
	else:
		# filter_data = SearchQuerySet().filter(Q(event_startdate_time=datetime.now().date())|
		# 						   Q(event_enddate_time=datetime.now().date())) 	

		filter_data = Postevent.objects.filter(Q(event_startdate_time=datetime.now().date())|
								   Q(event_enddate_time=datetime.now().date()))								    								    							  
	for filter_datas in filter_data:
		# data = {'id':filter_datas.id.split('.')[-1],'title':filter_datas.eventtitle}
		data = {'id':filter_datas.id,'title':filter_datas.event_title}
		results.append(data)
		
	return HttpResponse(simplejson.dumps(results), mimetype='application/json')