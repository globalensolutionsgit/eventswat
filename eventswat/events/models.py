from django.contrib.auth.models import *
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from haystack.query import SearchQuerySet
from events.extra import ContentTypeRestrictedFileField
from datetime import datetime
import os
from django.conf import settings

class DateAbstract(models.Model):
	created_date=models.DateTimeField(max_length=50,auto_now_add=True)
	modified_date=models.DateTimeField(max_length=50, auto_now=True)

	class Meta:
		abstract = True

class EventsCategory(models.Model):
	"""
	This model for list of categories,icon path and hover_icon paths.Icons in media folders 
	"""
	category_name= models.CharField(max_length=150, unique=True)
	category_icon= models.ImageField(upload_to='category/icon/',max_length=100, default='')
	category_hover_icon= models.ImageField(upload_to='category/icon/',max_length=100, default='')

	def __unicode__(self):
		return self.category_name

class EventsSubCategory(models.Model):
	"""
	This model store the subcategory for multiple categories.Icons stores into media folders
 	"""
	category = models.ManyToManyField(EventsCategory)
	subcategory_name = models.CharField(max_length=50)
	subcategory_icon= models.ImageField(upload_to='subcategory/icon/',max_length=100) 
	subcategory_hover_icon= models.ImageField(upload_to='subcategory/icon/',max_length=100) 
	
	def __unicode__(self):
		return self.subcategory_name

class SubcategoryRelatedField(models.Model):
	"""docstring for ClassName"""
	field_name = models.CharField(max_length=100)
	related_subcategory = models.ManyToManyField(EventsSubCategory)
	
	def __unicode__(self):
		return self.field_name

class City(models.Model):
	city=models.CharField(max_length=150, default='')
	state=models.CharField(max_length=100, default='')
	country_code=models.CharField(max_length=10, null=True)
	country_name=models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.city

# class CollegeDepartment(models.Model):
# 	department=models.ForeignKey(CampusDepartment, null=True)
# 	college=models.ManyToManyField(CampusCollege,null=True)
# 	def __unicode__(self):
# 		return self.department.department

