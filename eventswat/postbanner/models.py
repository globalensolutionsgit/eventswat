from datetime import timedelta,datetime
from django.db import models
from events.extra import ContentTypeRestrictedFileField
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from usermanagement.models import Userprofile


POSITION = (
    ('bottom', 'Bottom of the page'),
    ('left', 'Left of the page'),
    ('right', 'Right of the page'),
)

PAGEURL=(
    ('/','Home page'),
    ('event/','Listing page'),
    ('details/','Details page'),
)

class BannerPlan(models.Model):
    page=models.CharField(max_length=50,choices=PAGEURL)
    position=models.CharField(max_length=50,choices=POSITION)
    price = models.FloatField(null=True, default=0.0)   
    plan_duration=models.BigIntegerField(null=True, blank=True,help_text="No of days allowed")

    class Meta:
        unique_together = [("page", "position")]

    def __unicode__(self):
        return self.position

class PostBanner( models.Model ):
    user=models.ForeignKey(Userprofile) 
    banner = ContentTypeRestrictedFileField(upload_to='static/banners',content_types=['image/jpeg','image/png'],max_upload_size=2097152,help_text="Please upload the banner Image with 2MB min and jpg, png format only allowed")
    link= models.CharField(max_length=200, null=True, blank=True, help_text="Please enter the website link")
    pageurl= models.CharField(max_length=50, choices=PAGEURL, help_text="Please select the page to display the banner")
    position=models.CharField(max_length=50, choices=POSITION, help_text="Please select the position to display the banner")
    bannerplan=models.ForeignKey(BannerPlan)
    startdate= models.DateTimeField(default=datetime.now(),help_text="Startdate for banner") 
    enddate = models.DateTimeField(default=datetime.now()+timedelta(days=30),help_text="Enddate for banner") 
    duration=models.IntegerField(null=True, blank=True, help_text="No of days allowed")
    admin_status = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    def __unicode__(self):
        return self.link

    def save(self): 
        filterargs = { 'page': self.pageurl, 'position': self.position }
        try:
            result = BannerPlan.objects.get(**filterargs)
            self.price=result.price
            super(PostBanner, self).save()
        except:
            return HttpResponseRedirect('/admin/banner/PostBanner/')

# class Mainbanner(models.Model):
#     mainbanner = ContentTypeRestrictedFileField(upload_to='static/mainbanner',content_types=['image/jpeg','image/png'],max_upload_size=2097152,help_text="Please upload the Main banner Image with 2MB min and jpg, png format only allowed")
#     price=models.FloatField(null=True, help_text="Please enter the price as INR")
#     admin_status = models.BooleanField(default=False)

