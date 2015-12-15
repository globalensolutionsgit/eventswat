from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files import File
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import authenticate, login,logout
from django.template import Context
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.utils.encoding import smart_unicode, force_unicode
from eventswat.models import *
from eventswat.forms import *
from eventswat.util import format_redirect_url
from postbanner.models import *
from events.models import *
from events.views import *
from events.forms import EventSearchForm
import simplejson as json
import random
import string
import datetime

class JSONResponse(HttpResponse):
	def __init__(self, data):
		super(JSONResponse, self).__init__(
				simplejson.dumps(data), mimetype='application/json')

def find_position(request):	
	if request.is_ajax() and request.GET and 'path' in request.GET:
		if request.GET['path']== 'home':
			path='/'
		elif request.GET['path']== 'list':
			path='event/'
		else:
			path='details/'
		objs = BannerPlan.objects.filter(page=path)		
		return JSONResponse([{'id': o.id, 'name': smart_unicode(o.position)} for o in objs])
	else:
		return JSONResponse({'error': 'Not Ajax or no GET'})

def find_price(request):	
	if request.GET and 'path' and 'position' in request.GET:
		if request.GET['path']== 'home':
			path='/'
		elif request.GET['path']== 'list':
			path='event/'
		else:
			path='details/'
		filterargs = { 'page': path, 'position': request.GET['position'] }
		objs = BannerPlan.objects.filter( **filterargs)		
		return JSONResponse([{'id': o.id, 'name': smart_unicode(o.price)} for o in objs])
	else:
		return JSONResponse({'error': 'Not Ajax or no GET'})