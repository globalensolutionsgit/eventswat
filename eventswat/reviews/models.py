import datetime
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from events.models import *
from datetime import datetime

class WebsiteFeedback(models.Model):
	name= models.CharField(max_length=50, null=True)
	email= models.EmailField(max_length=50)
	comments= models.TextField()
	rating=models.IntegerField()

class Review(models.Model):
    name =  models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(null = True, blank= True)  
    content = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now(), blank=True)   
    event_id = models.CharField(max_length=255, null=True,
                             blank=True)
    