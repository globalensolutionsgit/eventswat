import re
from django import forms
from collections import OrderedDict
from events.models import *
from haystack.forms import SearchForm, FacetedSearchForm
from datetime import datetime, timedelta
from django.http import HttpResponse, Http404
from search.searchresults import searchresults as eventsearch
from haystack.query import SearchQuerySet
from haystack.inputs import Clean, Raw, AutoQuery, Exact
from haystack.query import SQ
from postevent.models import Postevent
from django.db.models import Q

class Partial(Clean):
	input_type_name = 'partial'
	post_process = True

	def __init__(self, query_string, **kwargs):
		self.original = query_string
		super(Partial, self).__init__(query_string, **kwargs)

	def prepare(self, query_obj):
		# query_string = super(Partial, self).prepare(query_obj)
		query_string = query_string.lower()
		query_string = re.sub( '\s+', '* ', query_string).strip()

		if query_string[-1] != '*':
		  query_string = query_string + u'*'

		return 

class EventSearchFilter(FacetedSearchForm):
	model = None

	eventcategory = forms.IntegerField(required=False)
	eventsubcategory = forms.IntegerField(required=False)		
	city = forms.CharField(required=False)		
	eventtitle = forms.CharField(required=False)
	payment = forms.CharField(required=False)
	filterdata = forms.CharField(required=False)
	eventtype = forms.CharField(required=False)
	admin_status = forms.IntegerField(required=False)
  
	def get_default_filters(self):
	  sqs = SearchQuerySet().all()
	  sqs = sqs.models(Postevent)
	  return sqs

	def get_default_search_field(self):
	  return 'searchtext'

	def get_model_class(self):
	  return Postevent

	def search(self):
	  if not hasattr(self, 'cleaned_data'):
		return eventsearch(model_cls=self.get_model_class(), 
		  default_filters=self.get_default_filters())
		
	  _params = [
		'eventcategory',
		'eventsubcategory',
		'city',
		'eventtitle',
		'payment',
		'filterdata',
		'eventtype',
	  ]
	  params = OrderedDict()
	  for p in _params:
		if p in self.cleaned_data and self.cleaned_data[p]:
		  params[p] =  self.cleaned_data[p]
		else:
		  params[p] =  None

	  if params['eventcategory']:
		params['eventcategory'] = params['eventcategory']
		  
	  if params['eventsubcategory']:
		params['eventsubcategory'] = params['eventsubcategory']

	  if params['city']:
		params['city'] = params['city']

 
	  q = self.cleaned_data['q'] if 'q' in self.cleaned_data else None
	  groupby = None
	  orderby = None

	  orderby_mappings = {
		'payment':'-payment'
	  }
	  
	  # if self.cleaned_data['groupby']:
	  #   groupby = self.cleaned_data['groupby']

	 #  if self.cleaned_data['sorteddata']:
		# orderby = self.cleaned_data['sorteddata']
		# if orderby in orderby_mappings:
		#   orderby = orderby_mappings[groupby]

	  if not orderby:
		orderby = orderby_mappings['payment']

	  return eventsearch(q, params, orderby, groupby, model_cls=self.get_model_class(), 
		default_filters=self.get_default_filters(), 
		default_search_field=self.get_default_search_field())


