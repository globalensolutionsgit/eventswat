from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from events.views import *
from events.models import *
from django.views.generic import RedirectView
# Custom Search View
from search.eventsearch import EventSearchView
from search.searchform import EventSearchFilter

#For loading global functions
from django.template.loader import add_to_builtins
add_to_builtins('events.templatetags.app_filters')

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'events.views.home', name='home'),
	 # User login verfication
	url(r'^login/$', 'events.views.user_login', name='user_login'),
	url(r'^logout/$', 'events.views.logout_view', name='logout_view'),
	#registeration
	url(r'^register/$', 'events.views.register', name='register'),
	# for registeration confirm
	# url(r'^confirm/$', 'events.views.confirm', name='confirm'),

	# forget password
	url(r'^(?i)password_reset/$', 'django.contrib.auth.views.password_reset', {
	  'template_name':'registration/password_reset_form.html',
	  'email_template_name':'registration/password_reset_email.html'
	}, name="password_reset"),
	url(r'^(?i)user/password/reset/$',
		'django.contrib.auth.views.password_reset',
		{'post_reset_redirect' : '/user/password/reset/done/'}),
	url(r'^(?i)user/password/reset/done/$',
		'django.contrib.auth.views.password_reset_done'),
	url(r'^(?i)user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
		'django.contrib.auth.views.password_reset_confirm',
		{'post_reset_redirect' : '/user/password/done/'}),
	url(r'^(?i)user/password/done/$',
		'django.contrib.auth.views.password_reset_complete'),

	 # getting started
	url(r'^start/$', 'events.views.start',name='start'),
	url(r'^post_event$', 'events.views.post_event', name='post_event'),
	# url(r'^banner$', 'events.views.banner', name='banner'),
	url(r'^submit_event_v2$', 'events.views.submit_event_v2', name='submit_event_v2'),
	# url(r'^upload_banner$', 'events.views.upload_banner', name='upload_banner'),
	url(r'^success$', 'events.views.success', name='success'),
	url(r'^about$', 'events.views.about', name='about'),
	url(r'^feed/$', 'reviews.views.feedback', name='feedback'),
	url(r'^privacy_and_policy$', 'events.views.privacy_and_policy', name='privacy_and_policy'),
	url(r'^terms_and_conditions$', 'events.views.terms_and_conditions', name='terms_and_conditions'),
	url(r'^faqs$', 'events.views.faqs', name='faqs'),
	# url(r'^(?i)event/(?P<pname>.*)/$', 'events.views.event',name='event'),
	url(r'^details/(?P<id>[0-9]+)/$','events.views.details',name='details'),
	#url(r'^payment/', 'payu.views.buy_order', name='payment'),
	#url(r'^payment_event/', 'payu.views.paid_user', name='payment'),
	#getting subcategory
	url(r'^subcategory_for_category/$', 'events.views.subcategory_for_category',name='subcategory'),
	url(r'^all_subcategory_for_category/$', 'events.views.all_subcategory_for_category',name='all_subcategory'),

	# Find event when ajax call
	url(r'^event_for_subcategory/$', 'events.views.event_for_subcategory',name='event'),

	# Search & Advance Search
	url(r'^(?i)search/', EventSearchView(
	  template='search-result.html',
	  form_class=EventSearchFilter,
	  #results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
	), name='newsearchPageV2'),

	url(r'^(?i)ajax_search/', EventSearchView(
	  template='index_v2.html',
	  form_class=EventSearchFilter,
	  #results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
	), name='newsearchPageV2'),

	# url(r'^blog/', include('blog.urls')),

	url(r'^find_colleges/$', 'events.views.find_colleges',name='find_colleges'),
	url(r'^find_department/$', 'events.views.find_department',name='find_department'),
	url(r'^find_subcategory/$', 'events.views.find_subcategory',name='find_subcategory'),
	url(r'^find_city/$', 'events.views.find_city',name='find_city'),
	url(r'^getcity/$', 'events.views.getcity',name='getcity'),
	url(r'^getstate/$', 'events.views.getstate',name='getstate'),
	url(r'^getcollege/$', 'events.views.getcollege',name='getcollege'),
	url(r'^getdept/$', 'events.views.getdept',name='getdept'),
	url(r'^getcity_base/$', 'events.views.getcity_base',name='getcity_base'),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^import/', 'events.views.importcollegedata', name='importcollegedata'),
	# url('', include('social.apps.django_app.urls', namespace='social')),
   	url('', include('django.contrib.auth.urls', namespace='auth')),
   	url(r'^home_v2/$', 'events.views.home_v2', name='home_v2'),
   	url(r'^comment/',  'reviews.views.comment', name='comment'),
   	# url(r'^post/$', 'reviews.views.post_review', name='reviews-post-review'),

   	url(r'^get_events_for_calendar/',  'events.views.get_events_for_calendar', name='eventcalendar'),
	url(r'^admin_subcategory/','postevent.views.admin_subcategory',name='admin_subcategory'),
	#url(r'^admin/postevnet',include('postevent.urls')),
   	url(r'^add_google_calendar/(?P<id>[0-9]+)/$', 'events.views.add_google_calendar', name='add_google_calendar'),

   	# for socail_auth and tracking module by priya
   	url(r'^tracking/', include('tracking.urls')),
	url(r'', include('payu.urls')),
   	# url(r'^social/', include('social_auth.urls')),
   	url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
    url(r'^login-error/$', LoginError.as_view()),
   	url(r'^(?i)postevent/', include('postevent.urls')),
   	url(r'^(?i)payu/', include('payu.urls')),
   	url(r'', include('usermanagement.urls')),
   	url(r'', include('postbanner.urls')),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
