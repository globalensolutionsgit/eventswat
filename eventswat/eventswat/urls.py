from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from search.eventsearch import EventSearchView
from search.searchform import EventSearchFilter

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'eventswat.views.home', name='home'),
	url(r'^listpage/$', 'eventswat.views.listpage', name='listpage'),
	# Search & Advance Search     
	url(r'^(?i)search/', EventSearchView(
	  template='search/searchlist.html', 
	  form_class=EventSearchFilter, 
	  #results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
	), name='newsearchPageV2'), 

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
