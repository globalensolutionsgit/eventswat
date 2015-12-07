from django.contrib.auth.models import User
from django.db import models
from eventswat.models import *
from events.models import *
from postevent.models import *
SELECT_GENDER = (
	('male','Male'),
	('female','Female'),
	)

SELECT_USER_TYPE = (
	('institution','Institution'),
	('organization','Organization'),
	('corporate','Corporate'),
	)

#Model for storing user personal details
class Userprofile(User):
	date_of_birth = models.DateField(null=True, blank=True)
	mobile=models.CharField(max_length=50)
	gender = models.CharField(max_length=50, null=True, blank=True, choices=SELECT_GENDER)
	user_address= models.TextField(null=True, blank=True)
	verification_code=models.CharField(max_length=500, blank=True)
	is_emailverified=models.BooleanField(default=False)
	user_interest=models.ManyToManyField(EventsSubCategory)
	twitter_url  =models.CharField(max_length=200, blank=True)
	facebook_url =models.CharField(max_length=200, blank=True)
	user_type=models.CharField(max_length=50, null=True, blank=True, choices=SELECT_USER_TYPE)
	profile_pic = models.ImageField(upload_to='/static/img/',null=True, blank=True, max_length=500)
	
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username 

