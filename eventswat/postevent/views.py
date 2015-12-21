from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import smart_unicode, force_unicode
from django.utils import simplejson
from haystack.query import SearchQuerySet
from django.db.models import Q

def getevents_by_date(request):
	results = SearchQuerySet().filter(Q(event_startdate_time=request.GET.get('date'))|
								   Q(event_enddate_time=request.GET.get('date'))
								   ) 
	print "results", results
	return HttpResponse(simplejson.dumps(smart_unicode(results)), mimetype='application/json')