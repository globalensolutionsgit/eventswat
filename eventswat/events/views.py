from django.http import HttpResponseRedirect, HttpResponse
from models import City

def getcity_base(request):
	from collections import OrderedDict
	results = []
	unsort_dict = {}
	key_loc = request.GET.get('term')
	city_lists = City.objects.filter(city__icontains= key_loc)

	for city_list in city_lists:
		cityname = city_list.city.strip()
		cityid = city_list.id
		unsort_dict[cityname] = {'cityid':cityid, 'label':cityname, 'value':cityname}

	sorted_dic = OrderedDict(sorted(unsort_dict.iteritems(), key=lambda v: v[0]))
	for k, v in sorted_dic.iteritems():  
		results.append(v)

	return HttpResponse(simplejson.dumps(results), mimetype='application/json')