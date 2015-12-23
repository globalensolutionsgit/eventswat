from django.contrib.auth.models import User
from django.db import models
from eventswat.models import *
from events.models import *
from postevent.models import *

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)


USER_TYPE_CHOICES = (
    ('institution', 'Institution'),
    ('organization', 'Organization'),
    ('corporate', 'Corporate'),
)

# Model for storing user personal details


class Userprofile(User):
    """
    This is model is used for maintaining Userprofile for each 
    authenticated user
    """
    date_of_birth = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=True,
                              blank=True, choices=GENDER_CHOICES)
    user_address = models.TextField(null=True, blank=True)
    verification_code = models.CharField(max_length=500, blank=True)
    is_emailverified = models.BooleanField(default=False)
    user_interest = models.ManyToManyField(EventsSubCategory, blank=True)
    twitter_url = models.CharField(max_length=200, blank=True)
    facebook_url = models.CharField(max_length=200, blank=True)
    user_type = models.CharField(
        max_length=50, null=True, blank=True, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(
        upload_to='profile', null=True, blank=True, max_length=500)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.username

    class Meta:
        """
        used to set verbose_name as Userprofile
        """
        verbose_name = 'Userprofile'
