from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from search.eventsearch import EventSearchView
from search.searchform import EventSearchFilter
from postevent.views import *

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'eventswat.views.home', name='home'),
	url(r'^listpage/$', 'eventswat.views.listpage', name='listpage'),
	# Search & Advance Search     
	url(r'^(?i)search/', EventSearchView(
	  template='search/searchlist.html', 
	  form_class=EventSearchFilter, 
	), name='newsearchPageV2'), 
	url(r'^postevent/getevents_by_date/$', 'postevent.views.getevents_by_date', name='getevents_by_date'),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
