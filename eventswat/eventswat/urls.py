from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'eventswat.views.home', name='home'),
	url(r'^listpage/$', 'eventswat.views.listpage', name='listpage'),



)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
