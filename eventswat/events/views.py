from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.template import Context, RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _
from events.models import *
from usermanagement	.models import Userprofile
from usermanagement.forms import UserCreationForm, UserLoginForm
from events.extra import JSONResponse
from postevent.models import Postevent, Organizer, CampusCollege, CampusDepartment
from reviews.models import *
from reviews.forms import *
from postbanner.models import *
from payu.models import *
from eventswat.util import format_redirect_url
from templated_email import send_templated_mail
from forms import UploadFileForm
from django.utils.timezone import utc
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_auth.views import complete

try:
	import json
except ImportError:
	from django.utils import simplejson as json


@csrf_exempt
def home(request):
	registeration_form = UserCreationForm()
	login_form = UserLoginForm()
	feedback_form = WebsiteFeedbackForm()
	if request.user.is_superuser:
		logout(request)
		return HttpResponseRedirect('/')
	return render_to_response("index_v2.html", {'registeration_form': registeration_form, 'login_form': login_form, 'feedback_form': feedback_form}, context_instance=RequestContext(request))


def about(request):
	return render_to_response("about-us.html", context_instance=RequestContext(request))


def privacy_and_policy(request):
	return render_to_response("privacy.html", context_instance=RequestContext(request))


def terms_and_conditions(request):
	return render_to_response("terms_and_conditions.html", context_instance=RequestContext(request))


def faqs(request):
	return render_to_response("faqs.html", context_instance=RequestContext(request))


def start(request):
	return render_to_response('index_v2.html', context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	response = HttpResponseRedirect("/")
	return response

# comments implemented by priya
@csrf_exempt

def details(request,id=None):
	postevent=Postevent.objects.get(pk=id)
	userprofile = Userprofile()
	img=str(postevent.event_poster).split(',')
	photo=img[0]
	photos=[n for n in str(postevent.event_poster).split(',')]
	organizer=Organizer.objects.filter(postevent__id=postevent.id)
	registeration_form = UserCreationForm()
	login_form = UserLoginForm()
	comment_form = CommentForm()
	comment_tree=Comment.objects.filter(postevent_id=postevent.id).order_by('-path')
	return render_to_response("company-profile.html",{'comment_tree':comment_tree,'events':postevent,'organizer':organizer,'photos':photos,'photo':photo, 'registeration_form':registeration_form, 'login_form':login_form, 'comment_form':comment_form, 'userprofile':userprofile}, context_instance=RequestContext(request))

def banner(request):
	return render_to_response("uploadbanner.html",context_instance=RequestContext(request))

# login and registration implemanted by ramya
@csrf_exempt
def user_login(request):
	import json
	if request.user.is_superuser:
		logout(request)
		return HttpResponseRedirect('/')
	logout(request)
	error = {}
	login_form = UserLoginForm(request.POST)
	if request.method == 'POST' and login_form.is_valid():		
		context = {}
		if not User.objects.filter(email=login_form.cleaned_data['login_email']).exists():
			error['email_exists'] = True
			response = HttpResponse(json.dumps(error, ensure_ascii=False),mimetype='application/json')
			return response

		else:
			user = User.objects.get(email=login_form.cleaned_data['login_email'])
			user.backend='django.contrib.auth.backends.ModelBackend'
			if user is not None:			
				if user.check_password(login_form.cleaned_data['login_password']):
					if user.is_active:
						login(request, user)
						response = HttpResponseRedirect(request.POST.get('next'))
				else:
					error['password'] = True
					response = HttpResponse(json.dumps(error, ensure_ascii=False),mimetype='application/json')
					return response
	else:
		login_form = UserLoginForm()
	return render_to_response('index_v2.html', {'login_form':login_form}, context_instance=RequestContext(request))

@csrf_protect
def register(request):
	registered = False
	user=User()
	userprofile=Userprofile()
	registeration_form = UserCreationForm(request.POST)
	if request.method == 'POST' and registeration_form.is_valid():		
		username = registeration_form.data.get('username')
		email = registeration_form.cleaned_data['email']
		try:
			error={}
			if Userprofile.objects.filter(username=username).exists():
				error['username_exists'] = ugettext('Username already exists')
			if Userprofile.objects.filter(email=email).exists():
				error['email_exists'] = ugettext('Email already exists')
				raise ValidationError(error['email_exists'], 2)

		except ValidationError as e:
			messages.add_message(request, messages.ERROR, e.messages[-1])
			redirect_path = "/"
			query_string = 'rst=%d' % e.code
			redirect_url = format_redirect_url(redirect_path, query_string)
			return HttpResponseRedirect(redirect_url)

		if not error:
			userprofile.is_active = True
			userprofile = registeration_form.save()
			send_templated_mail(
			  template_name = 'welcome',
			  subject = 'Welcome Evewat',
			  from_email = 'eventswat@gmail.com',
			  recipient_list = [email],
			  context={
					   'userprofile': username,
			  },
			)
			registered = True
			registered_user = Userprofile.objects.get(email= email)
			registered_user.backend='django.contrib.auth.backends.ModelBackend'
			login(request, registered_user)
			return HttpResponseRedirect('/start/?user_id=' + str(registered_user.id))

		elif userprofile.id is None:
			return HttpResponseRedirect('/')

	else:
		registeration_form = 	UserCreationForm()
		user_id = userprofile.id
	return render_to_response('index_v2.html', {'user_id':user_id, 'registeration_form':registeration_form } ,context_instance=RequestContext(request))


class AuthComplete(View):

	def get(self, request, *args, **kwargs):
		backend = kwargs.pop('backend')
		try:
			return complete(request, backend, *args, **kwargs)
		except:
			messages.error(
				request, "Your Google Apps domain isn't authorized for this app")
			return HttpResponseRedirect(reverse('login'))


class LoginError(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse(status=401)
