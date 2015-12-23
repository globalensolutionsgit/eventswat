from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from usermanagement	.models import Userprofile
from usermanagement.forms import UserCreationForm, UserLoginForm
from postevent.models import Postevent
from events.models import EventsSubCategory
from django.conf import settings


@csrf_exempt
def user_profile(request):
    if request.user.is_authenticated():
        requested_user = User.objects.get(email=request.user.email)
        print 'requested_user', requested_user
        if request.method == 'POST':
            print 'POST'
            gender = request.POST.get('gender', '')
            date_of_birth = request.POST.get('dob')
            if date_of_birth == '':
                date_of_birth = None
            print 'date_of_birth', date_of_birth
            user_address = request.POST.get('address', '')
            user_interest = request.POST.get('user_interest', '')
            twitter_url = request.POST.get('twitter_url', '')
            facebook_url = request.POST.get('facebook_url', '')
            user_type = request.POST.get('user_type', '')

            def handle_uploaded_file(f):
                print "settings.MEDIA_ROOT", settings.MEDIA_ROOT
                profile_picture = open(
                    settings.MEDIA_ROOT + '/profile/' + '%s' % f.name, 'wb+')
                for chunk in f.chunks():
                    profile_picture.write(chunk)
                profile_picture.close()

            if 'profile_poster' in request.FILES:
                profile_picture = request.FILES['profile_poster']
                print 'profile_picture', profile_picture
                handle_uploaded_file(profile_picture)
                profile_picture = '/profile/' + str(profile_picture)

            if Userprofile.objects.filter(email=requested_user.email).exists():
                print 'yes'
                user_id = Userprofile.objects.get(email=requested_user.email)
                user_id.gender = gender
                user_id.date_of_birth = date_of_birth
                print'date_of_birth', user_id.date_of_birth
                user_id.user_address = user_address
                if 'profile_poster' in request.FILES:
                    user_id.profile_pic = request.FILES['profile_poster']
                    print 'if pic', user_id.profile_pic
                user_id.twitter_url = twitter_url
                user_id.facebook_url = facebook_url
                user_id.user_type = user_type
                user_id.user_interest = user_interest
                user_id.save()
        try:
            print 'try'
            requested_user_profile = Userprofile.objects.get(
                email=requested_user.email)
            print 'requested_user_profile mobile', requested_user_profile
            event_interest = EventsSubCategory.objects.all()
            events_for_user = Postevent.objects.filter(
                user_email=request.user.email)
            print 'events_for_user', events_for_user
            return render_to_response("user_profile.html",
                                      {'requested_user': requested_user,
                                       'requested_user_profile': requested_user_profile,
                                       'events_for_user': events_for_user,
                                       'event_interest': event_interest},
                                      context_instance=RequestContext(request))
        except:
            events_for_user = Postevent.objects.filter(
                user_email=request.user.email)
            print 'events_for_user', events_for_user
            event_interest = EventsSubCategory.objects.all()
            return render_to_response("user_profile.html",
                                      {'requested_user': requested_user,
                                       'events_for_user': events_for_user,
                                       'event_interest': event_interest},
                                      context_instance=RequestContext(request))


@csrf_exempt
def privacy(request):
    if request.user.is_authenticated():
        print 'request.user.email', request.user.email
        u = User.objects.get(email=request.user.email)
        new_password = request.POST.get('newpassword')
        u.set_password(new_password)
        u.save()
        return render_to_response("user_profile.html",
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
