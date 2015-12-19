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

# @csrf_exempt
# @login_required(login_url='/?lst=2')
# def upload_banner(request):
# 	if request.POST.get('price',False):
# 		uploadbanner=PostBanner()
# 		# uploadbanner.price=request.POST.get('price',request.COOKIES.get('price'))
# 		uploadbanner.position=request.POST.get('position',request.COOKIES.get('position'))
# 		uploadbanner.pageurl=request.POST.get('pageurl',request.COOKIES.get('pageurl'))
# 		uploadbanner.banner=request.FILES.get('banner',request.COOKIES.get('banner'))
# 		uploadbanner.link=request.POST['link']
# 		uploadbanner.save()
# 		send_templated_mail(
# 			  template_name = 'banner',
# 			  subject = 'Uplaod Banner',
# 			  from_email = 'eventswat@gmail.com',
# 			  recipient_list = [request.user.email ],
# 			  context={
# 					   'user': request.user,

# 			  },
# 		  )
# 		response=HttpResponseRedirect("/payment/")
# 		# response.set_cookie( 'price', uploadbanner.price )
# 		response.set_cookie( 'position', uploadbanner.position )
# 		response.set_cookie( 'banner', uploadbanner.banner )
# 		response.set_cookie( 'pageurl', uploadbanner.pageurl )
# 	#field9 is payu success variable
# 	# this if condition for after success of payment
# 	elif 'field9' in request.POST:
# 		message="Your data succesfully uploaded"
# 		response = render_to_response("uploadbanner.html",{'message':message},context_instance=RequestContext(request))
# 	else:
# 		message="Something went to wrong"
# 		response = render_to_response("uploadbanner.html",{'message':message},context_instance=RequestContext(request))
# 	return response

# @csrf_exempt
# def success(request):
# 	#field9 is payu success variable
# 	# this if condition for after success of payment
# 	if 'field9' in request.POST:
# 		response = render_to_response("success.html",context_instance=RequestContext(request))
# 		response.delete_cookie('eventtitle')
# 		response.delete_cookie('startdate')
# 		response.delete_cookie('enddate')
# 		response.delete_cookie('plan')
# 		response.delete_cookie('category_name')
# 		response.delete_cookie('eventtype_name')
# 		response.delete_cookie('eventtype')
# 		response.delete_cookie('category')
# 		response.delete_cookie('eventdescription')
# 	else:
# 		response =HttpResponseRedirect('/')
# 	return response
