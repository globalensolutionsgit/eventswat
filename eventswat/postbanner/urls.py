from django.conf.urls import patterns, url
from postbanner.views import *

urlpatterns = patterns('',
                       url(r'^banner/$', 'postbanner.views.banner',
                           name='banner'),
                       url(r'^upload_banner/$',
                           'postbanner.views.upload_banner',
                           name='upload_banner'),
                       )
