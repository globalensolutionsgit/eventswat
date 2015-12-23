from django.conf.urls import patterns, url
from usermanagement.views import *

urlpatterns = patterns('',
	url(r'^user_profile/',  'usermanagement.views.user_profile', name='user_profile'),
	url(r'^privacy/', 'usermanagement.views.privacy', name='privacy'),
)
	