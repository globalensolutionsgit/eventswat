from django.db import models
from datetime import datetime
from postevent.models import Postevent
from django.core.validators import MinValueValidator, MaxValueValidator


class WebsiteFeedback(models.Model):
	""" Getting users feedback for our site"""
	name= models.CharField(max_length=50, null=True)
	email= models.EmailField(max_length=50)
	comments= models.TextField()
	rating=models.IntegerField()


class Comment(models.Model):
	""" Getting comment for particular events"""
	content = models.TextField(blank=False, null=True)
	date = models.DateTimeField(auto_now_add=True)
	path = models.CharField(blank=True, max_length=500, editable=False)
	depth = models.PositiveSmallIntegerField(default=0)
	rating=models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0),
									   MaxValueValidator(5)])
	#postevent = models.ForeignKey(Postevent)

	def __unicode__(self):
		return self.content
