from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from search.eventsearch import EventSearchView
from search.searchform import EventSearchFilter
from postevent.views import *

from django.template.loader import add_to_builtins
add_to_builtins('events.templatetags.app_filters')
admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'eventswat.views.home', name='home'),

                       # user authentication
                       url(r'^start/$', 'eventswat.views.start',name='start'),
                       url(r'^login/$', 'eventswat.views.user_login',
                           name='user_login'),
                       url(r'^logout/$', 'eventswat.views.logout_view',
                           name='logout_view'),
                       url(r'^register/$', 'eventswat.views.register',
                           name='register'),

                       # Search & Advance Search
                       url(r'^(?i)search/', EventSearchView(
                           template='search/searchlist.html',
                           form_class=EventSearchFilter,
                       ), name='newsearchPageV2'),
                       url(r'^(?i)postevent/', include('postevent.urls')),
                       url(r'^postevent/getevents_by_date/$',
                           'postevent.views.getevents_by_date',
                           name='getevents_by_date'),
                       url(r'^getcity_base/$', 'events.views.getcity_base',
                           name='getcity_base'),
                       url(r'^get_event_title/$',
                           'events.views.get_event_title',
                           name='get_event_title'),

                       # forget password and reset password

                       url(r'^(?i)password_reset/$', 
                          'django.contrib.auth.views.password_reset', {
                           'template_name': 'registration/password_reset_form.html',
                           'email_template_name': 'registration/password_reset_email.html'
                       }, name="password_reset"),
                       url(r'^(?i)user/password/reset/$',
                           'django.contrib.auth.views.password_reset',
                           {'post_reset_redirect': '/user/password/reset/done/'}),
                       url(r'^(?i)user/password/reset/done/$',
                           'django.contrib.auth.views.password_reset_done'),
                       url(r'^(?i)user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           {'post_reset_redirect': '/user/password/done/'}),
                       url(r'^(?i)user/password/done/$',
                           'django.contrib.auth.views.password_reset_complete'),

                       #payu module
                       url(r'^(?i)payu/', include('payu.urls')),

                       #post banner module
                       url(r'', include('postbanner.urls')),

                       ) + static(settings.MEDIA_URL,
                                  document_root=settings.MEDIA_ROOT)
