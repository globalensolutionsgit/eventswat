from django.http import HttpResponseRedirect, HttpResponse
from models import City
from django.utils import simplejson
from postevent.models import Postevent

def getcity_base(request):
	from collections import OrderedDict	
	results = []
	unsort_dict = {}
	key_loc = request.GET.get('term')	
	city_lists = City.objects.filter(city__icontains= key_loc)
	print 'city_list', city_lists

	for city_list in city_lists:
		cityname = city_list.city.strip()
		cityid = city_list.id
		unsort_dict[cityname] = {'cityid':cityid, 'label':cityname, 'value':cityname}

	sorted_dic = OrderedDict(sorted(unsort_dict.iteritems(), key=lambda v: v[0]))
	for k, v in sorted_dic.iteritems():  
		results.append(v)
	return HttpResponse(simplejson.dumps(results), mimetype='application/json')

def get_event_title(request):
	from collections import OrderedDict	
	results = []
	unsort_dict = {}
	key_title = request.GET.get('term')	
	titles = Postevent.objects.filter(event_title__contains=key_title)
	
	for title in titles:
		event_name = title.event_title.strip()
		eventid = title.id
		unsort_dict[event_name] = {'eventid':eventid, 'label':event_name, 'value':event_name}

	sorted_dic = OrderedDict(sorted(unsort_dict.iteritems(), key=lambda v:v[0]))
	for k,v in sorted_dic.iteritems():
		results.append(v)
	return HttpResponse(simplejson.dumps(results), mimetype='application/json')	