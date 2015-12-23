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

	url(r'^admin/', include(admin.site.urls)),
	# url('', include('social.apps.django_app.urls', namespace='social')),
   	url('', include('django.contrib.auth.urls', namespace='auth')),
   	url(r'^comment/',  'reviews.views.comment', name='comment'),
   	# url(r'^post/$', 'reviews.views.post_review', name='reviews-post-review'),

   	# for socail_auth and tracking module by priya
   	url(r'^tracking/', include('tracking.urls')),
	url(r'', include('payu.urls')),
   	url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
    url(r'^login-error/$', LoginError.as_view()),
   	url(r'^(?i)postevent/', include('postevent.urls')),
   	url(r'^(?i)payu/', include('payu.urls')),
   	url(r'', include('usermanagement.urls')),
   	url(r'', include('postbanner.urls')),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
