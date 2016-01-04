from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from eventswat.util import format_redirect_url
from templated_email import send_templated_mail
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages

from django.contrib.auth.models import User
from usermanagement	.models import Userprofile
from usermanagement.forms import UserCreationForm, UserLoginForm


def home(request):
    registeration_form = UserCreationForm()
    login_form = UserLoginForm()
    return render_to_response('index.html', 
                             {'login_form':login_form, 
                             'registeration_form':registeration_form},
                             context_instance=RequestContext(request))

# login and registration implemanted by ramya

def logout_view(request):
    logout(request)
    response = HttpResponseRedirect("/")
    return response

def start(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

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
        if not User.objects.filter(
                email=login_form.cleaned_data['login_email']).exists():
            error['email_exists'] = True
            response = HttpResponse(json.dumps(
                error, ensure_ascii=False), mimetype='application/json')
            return response

        else:
            user = User.objects.get(
                email=login_form.cleaned_data['login_email'])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if user is not None:
                if user.check_password(
                        login_form.cleaned_data['login_password']):
                    if user.is_active:
                        login(request, user)
                        response = HttpResponseRedirect(
                            request.POST.get('next'))
                else:
                    error['password'] = True
                    response = HttpResponse(json.dumps(
                        error, ensure_ascii=False),
                        mimetype='application/json')
                    return response
    else:
        login_form = UserLoginForm()
    return render_to_response('index.html', {'login_form': login_form},
                              context_instance=RequestContext(request))


@csrf_protect
def register(request):
    registered = False
    user = User()
    userprofile = Userprofile()
    registeration_form = UserCreationForm(request.POST)
    if request.method == 'POST' and registeration_form.is_valid():
        username = registeration_form.data.get('username')
        email = registeration_form.cleaned_data['email']
        try:
            error = {}
            if Userprofile.objects.filter(username=username).exists():
                error['username_exists'] = ugettext('Username already exists')
                raise ValidationError(error['username_exists'], 1)
            if Userprofile.objects.filter(email=email).exists():
                error['email_exists'] = ugettext('Email already exists')
                raise ValidationError(error['email_exists'], 2)

        except ValidationError as e:
            messages.add_message(request, messages.ERROR, e.messages[-1])
            redirect_path = '/'
            query_string = 'rst=%d' % e.code
            print 'query_string', query_string
            redirect_url = format_redirect_url(redirect_path, query_string)
            print 'redirect_url', redirect_url
            return HttpResponseRedirect(redirect_url)

        if not error:
            userprofile.is_active = True
            userprofile = registeration_form.save()
            send_templated_mail(
                template_name='welcome',
                subject='Welcome Evewat',
                from_email='eventswat@gmail.com',
                recipient_list=[email],
                context={
                    'userprofile': username,
                },
            )
            registered = True
            registered_user = Userprofile.objects.get(email=email)
            registered_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, registered_user)
            return HttpResponseRedirect(
                '/start/?user_id=' + str(registered_user.id))

        elif userprofile.id is None:
            return HttpResponseRedirect('/')

    else:
        registeration_form = UserCreationForm()
        user_id = userprofile.id
    return render_to_response('index.html',
                              {'user_id': user_id,
                               'registeration_form': registeration_form},
                              context_instance=RequestContext(request))
