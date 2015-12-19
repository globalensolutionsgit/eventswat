from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404

import models
# from actors.models import Actor

# from dateutil import tz
#from_zone = tz.tzutc()
# to_zone = tz.tzlocal()

class WorkerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'interval', 'wait_for_approval', 'active')
  list_filter = ['name', 'active']
  search_fields = ['name', 'cls_path', 'interval', 'wait_for_approval', 'active']
  pass

class WorkerTaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'worker', 'notes', 'worker_options', 'status', 'completed', 'modified')
  list_filter = ['worker', 'status']
  search_fields = ['worker', 'notes', 'worker_options', 'status']
  
  list_per_page = 100

class NoticeEmailConfigAdmin(admin.ModelAdmin):
  list_display = ('id', 'max_email_per_lead', 'email_per_sale', 'max_iterations', 'max_email_retry', 'email_queue_limit')
  pass

admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.WorkerTask, WorkerTaskAdmin)
admin.site.register(models.UserTracking)
admin.site.register(models.NoticeEmailConfig, NoticeEmailConfigAdmin)
admin.site.register(models.WorkerNoticeEmailTask)
# admin.site.register(models.ProductEmailTracking)
admin.site.register(models.BannerExpiredAdTracking)


