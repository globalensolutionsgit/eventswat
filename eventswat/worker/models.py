from django.db import models
from events.models import *
from eventswat.models import *
from postbanner.models import *
from core import helper
from postevent.models import Postevent

WorkerTaskStatus = (
  ('init', 'Initialized'),
  ('wait_for_approval', 'Wait for Approval'),
  ('scheduled', 'Scheduled'),
  ('started', 'Started'),
  ('failed', 'Failed'),
  ('completed', 'Completed'),
  ('canceled', 'Canceled')
)

class Worker(models.Model):

  id = models.CharField(max_length=128, unique=True, primary_key=True)
  name = models.CharField(max_length=128)
  cls_path = models.CharField(max_length=512)

  interval = models.BigIntegerField(default=60*5, help_text="interval in seconds")
  wait_for_approval = models.BigIntegerField(default=60*60*2, help_text="prepare the task and wait for approval")
  notify_for_approval = models.CharField(max_length=2048, blank=True, null=True, help_text="List email id to notify")
  notify_for_errors = models.CharField(max_length=2048, blank=True, null=True, help_text="List email id to notify")

  options = models.TextField(null=True, blank=True)
  active = models.BooleanField(default=True)

  @staticmethod
  def default_data():
    workers = Worker(id='postevent_notice_email')
    worker.name = 'Postevent Notice Email'
    worker.cls_path = 'worker.workers.EmailNotificationWorker'
    worker.save()

  def __unicode__(self):
    return self.id

class WorkerTask(models.Model):

  worker = models.ForeignKey(Worker)
  notes = models.TextField(null=True, blank=True)
  worker_options = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=64, choices=WorkerTaskStatus, default='init')
  scheduled = models.DateTimeField(blank=True, null=True)
  started = models.DateTimeField(blank=True, null=True)
  completed = models.DateTimeField(blank=True, null=True)
  modified = models.DateTimeField(auto_now_add=True, auto_now=True)


class UserTracking(models.Model):
  track_alert = models.ForeignKey(Postevent)
  email_sent_count = models.PositiveIntegerField(default=0, help_text="Total number of email sent to this user")
  email_read_count = models.PositiveIntegerField(default=0, help_text="Number of times user have read an email")
  email_view_count = models.PositiveIntegerField(default=0, help_text="Number of times user have clicked the link")
  recent_email_fail_count = models.PositiveIntegerField(default=0)  
  last_email_sent = models.DateTimeField(null=True)

class WorkerNoticeEmailTask(models.Model):

  task = models.ForeignKey(WorkerTask)
  postevent=models.ForeignKey(Postevent)
  tracking_code = models.CharField(max_length=256, blank=True, null=True)
  iteration_count = models.PositiveIntegerField(default=0)

class NoticeEmailConfig(models.Model):

  id = models.CharField(max_length=128, unique=True, primary_key=True)
  max_email_per_lead = models.PositiveIntegerField(default=0, help_text="Maximum number of email can be send per lead, If the value is zero, it will calculate based on number of sales and email_per_sale")
  email_per_sale = models.PositiveIntegerField(default=5)
  max_iterations = models.PositiveIntegerField(default=1, help_text="Number of iteration, notice email should run. At every iteration, it will email new users")

  max_email_retry = models.PositiveIntegerField(default=3, help_text="Maximum retry for a single actor")
  email_queue_limit = models.PositiveIntegerField(default=10, help_text="Notice email queue limit for a single actor")

  @staticmethod
  def default_data():
      NoticeEmailConfig(id='default').save()


  # @classmethod
  # def create(cls, created_alert):
  #   task = WorkerNoticeEmailTask.objects.filter(created_alert=created_alert)
  #   if task.count() == 0:
  #     worker = Worker.objects.get(pk='freealert_notice_email')
  #     wtask = WorkerTask(worker=worker)
  #     wtask.save()

  #     task = WorkerNoticeEmailTask(task=wtask, created_alert=created_alert, 
  #       tracking_code=helper.randomkey(26))
  #     task.save()
   
  def __unicode__(self):
    return str(self.created_alert.id)

class BannerExpiredAdTracking(models.Model):
  banner=models.ForeignKey(PostBanner)
  email_sent_count=models.PositiveIntegerField(default=0, help_text="Total number of email sent")
  last_email_sent = models.DateTimeField(null=True)






