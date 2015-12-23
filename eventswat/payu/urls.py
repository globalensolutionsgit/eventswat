from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^payment_success/$', 'payu.views.payu_data'),
)
