from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^payment/$', 'postbanner.views.payment'),
)
