from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^load_state/$', 'postevent.views.load_state'),
    url(r'^load_city/$', 'postevent.views.load_city'),
    url(r'^$', 'postevent.views.postevent'),
)
