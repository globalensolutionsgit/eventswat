import logging
import time
import traceback
import operator
from datetime import datetime, timedelta
from models import *
from django.conf import settings
from django.contrib.sites.models import Site
from postevent.models import Postevent
from django.contrib.auth.models import User
from templated_email import send_templated_mail
from core import  helper
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import smart_str
class WorkerBase(object):

	def __init__(self, worker):
		self.worker = worker

	def create_tasks(self):
		pass

	def prepare(self):
		pass

	def runtasks(self, tasks):
		pass

	def finish(self):
		pass

class EmailNotificationWorker(WorkerBase):

	def create_tasks(self):    
		print "create_tasks1"
		print self.worker
		workertask=WorkerTask.objects.get(worker=self.worker)

		workertask.status='init'
		workertask.save() 
		print "save"  
		print "self.worker", self.worker.id
		tasks = WorkerTask.objects.filter(worker=self.worker, status='init')
		print "tasks", tasks
		for task in tasks:
			print "task.worker", task.worker
		# config = NoticeEmailConfig.objects.get(pk='default')
		if tasks.count():
			print "Got tasks", tasks.count()
		for task in tasks:
			try:
				now  = helper.get_now()
				if self.worker.wait_for_approval:
					now = now + timedelta(seconds = self.worker.wait_for_approval)
				task.scheduled = now
				task.status = 'scheduled'
				task.save()

				# logging.debug("scheduled Lead for notice email : " + ntask.product.title)
			except Exception, e:
				logging.critical(e)
				traceback.print_exc()
				task.status = 'failed'
				task.notes = "Error while creating task " + traceback.format_exc()
				task.save() 
	 
	def runtasks(self, tasks):
		print "runtasks1"
		postevent=Postevent.objects.all()  
		for task in tasks:
			now = helper.get_now()
			task.status = 'started'
			task.started = now
			task.save()
			try:
				now  = helper.get_now()
				yesterday = now - timedelta(seconds=5)
				# yesterday = now - timedelta(hours=24)
				print "task", task
				for postevents in postevent:
					user=str(postevents.user_name)
					postevent_id = str(postevents.id)
					print "user",user
					print "postevent_id", postevent_id
					result= postevents.enddate
					print "result", result
					if result:       
						subject="Your " + str(postevents.event_title) + " Your event will be removed from today onwards"
						
					postevents.status_isactive = False      
					print postevents.user_email
					# ctx={'user':user}
					 
					send_templated_mail(
						template_name = 'welcome',
						subject = "subject",
						from_email = 'info@eventswat.com',
						recipient_list = [postevents.user_email],
						context = {'user':user},
							)
					print "mail sent successfully"
					task.status = 'completed'
					task.completed = helper.get_now()
					task.save()
					postevents.save()  
					

			except Exception, e:
				logging.critical(e)
				traceback.print_exc()
				task.status = 'failed'
				task.notes = "Error while running task " + traceback.format_exc()
				task.save()


class EmailNotification_ExpiredAds(WorkerBase):


  def create_tasks(self):    
    print "create_tasks"
    now  = helper.get_now()
    user=User()
    sitebanner=PostBanner.objects.all()

    for sitebanners in sitebanner:
      user_id=sitebanners.user_id
      print user_id
      user=User.objects.get(id=user_id)
      print user
      email=user.email
      print email
      name=user.username
      print name
      result=sitebanners.enddate
      print "result", result
      if result:       
        subject="Your " +  " Your banner will be removed from today onwards"
				
      sitebanners.admin_status = False 
      send_templated_mail(
						template_name = 'welcome',
						subject = "subject",
						from_email = 'info@eventswat.com',
						recipient_list = [email],
						context = {'name':name},
							)
      print "mail send" 
      sitebanners.save()

  def runtasks(self, tasks):
    print "runtasks"

 