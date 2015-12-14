from django.db import models
from events.models import *
from django.core.exceptions import ValidationError


class CampusCollege(models.Model):
    """Store colleges based on cities"""
    college_name = models.CharField(max_length=150, unique=True,help_text='Enter college name',verbose_name='College')
    city = models.ForeignKey(City,help_text='Select city name',verbose_name='City')

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"
        ordering = ['id']
        unique_together = ('college_name', 'city')

    def __unicode__(self):
        return self.college_name



class CampusDepartment(models.Model):
    """Store the department details"""
    department = models.CharField(max_length=150, unique=True,help_text='Enter Department',verbose_name='Department')
    college = models.ManyToManyField(CampusCollege,help_text='Choose what are the college has this department',verbose_name='College')
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['id']
    def __unicode__(self):
        return self.department


class PostEventKeyword(models.Model):
    """This model postevent related keywords"""
    keyword = models.CharField(max_length=50)

    def __unicode__(self):
        return self.keyword


class Postevent(models.Model):
    EVENT_MODE = (('free','Free'),('paid','Paid'),('nil','No Registration'),)
    event_type = models.CharField(max_length=50, choices=EVENT_MODE, default='free')
    event_category = models.ForeignKey(EventsCategory)
    event_subcategory = models.ForeignKey(EventsSubCategory)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    event_title = models.CharField(max_length=50)
    event_description = models.TextField()
    event_startdate_time = models.DateTimeField(max_length=50)
    event_enddate_time = models.DateTimeField(max_length=50)
    event_poster = models.ImageField(
        upload_to='static/img/',
        null=True,
        max_length=500,
        help_text="Please upload the banner Image with 2MB min and jpg, \
        png format only allowed")
    event_keywords = models.ManyToManyField(PostEventKeyword)
    terms_and_condition = models.TextField(null=True, blank=True)
    event_website = models.CharField(
        max_length=200,
        help_text='Enter the if event has website',
        blank=True,
        null=True)
    is_webinar = models.BooleanField(default=False)
    venue = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    # College And Department field will be remove after dump the data
    college = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_status = models.BooleanField(default=False)
    admin_status = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)

    def __unicode__(self):
        return self.event_title


class SubCategoryRelatedFieldValue(models.Model):
    postevent = models.ForeignKey(Postevent)
    subcategory_relatedfield = models.ForeignKey(SubcategoryRelatedField)
    field_value = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.field_value


class Organizer(models.Model):
    postevent = models.ForeignKey(Postevent)
    organizer_name = models.CharField(max_length=50)
    organizer_mobile = models.CharField(max_length=50)
    organizer_email = models.EmailField(max_length=50)

    def __unicode__(self):
        return self.organizer_name
