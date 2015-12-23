from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^admin_subcategory/$',
                           'postevent.views.admin_subcategory'),
                       url(r'^load_country/$', 'postevent.views.load_country'),
                       url(r'^load_state/$', 'postevent.views.load_state'),
                       url(r'^load_city/$', 'postevent.views.load_city'),
                       url(r'^$', 'postevent.views.postevent'),
                       url(r'^test/$', 'postevent.views.test'),
                       url(r'^save/$', 'postevent.views.save'),
                       )
