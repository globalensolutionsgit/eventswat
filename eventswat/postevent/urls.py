from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Newly added by kalai for getting events by specific date 
    # url(r'^getevents_by_date/$', 'postevent.views.getevents_by_date', name='getevents_by_date'),
)
