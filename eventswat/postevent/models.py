from django.db import models
from events.models import *
from django.core.exceptions import ValidationError


class CampusCollege(models.Model):
    """Store colleges based on cities"""
    college_name = models.CharField(
        max_length=150,
        unique=True,
        help_text='Enter college name',
        verbose_name='College')
    city = models.ForeignKey(
        City,
        help_text='Select city name',
        verbose_name='City')

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"
        ordering = ['id']
        unique_together = ('college_name', 'city')

    def __unicode__(self):
        return self.college_name


class CampusDepartment(models.Model):
    """Store the department details"""
    department = models.CharField(
        max_length=150,
        unique=True,
        help_text='Enter Department',
        verbose_name='Department')
    college = models.ManyToManyField(
        CampusCollege,
        help_text='Choose what are the college has this department',
        verbose_name='College')

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
    """This model store all the information about user posted events"""
    EVENT_MODE = (('free', 'Free'), ('paid', 'Paid'),
                  ('nil', 'No Registration'),)
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_MODE,
        default='free')
    event_category = models.ForeignKey(
        EventsCategory,
        help_text='Select event category .sub category will load \
                   automatically based on category',
        verbose_name='Category')
    event_subcategory = models.ForeignKey(
        EventsSubCategory,
        help_text='Select event subcategory',
        verbose_name='Sub category')
    user_name = models.CharField(
        max_length=50,
        help_text='Enter which user post event',
        verbose_name='User name')
    user_email = models.EmailField(
        max_length=50,
        help_text='Enter user valid email id',
        verbose_name='Email')
    user_mobile = models.CharField(
        max_length=50,
        help_text='Enter user active mobile number',
        verbose_name='Mobile')
    event_title = models.CharField(
        max_length=50,
        unique=True,
        help_text='Enter the event title or theme name',
        verbose_name='Event name')
    event_description = models.TextField(
        help_text='Please enter atleast 50 characters',
        verbose_name='Description')
    event_startdate_time = models.DateTimeField(
        max_length=50,
        help_text='Event start date and time.suggest for midnight',
        verbose_name='Start date')
    event_enddate_time = models.DateTimeField(
        max_length=50,
        help_text='Event end date and time.suggest for midnight',
        verbose_name='End date')
    event_poster = models.ImageField(
        upload_to='static/img/',
        null=True,
        max_length=500,
        help_text="Please upload the banner Image with 2MB min and jpg, \
        png format only allowed")
    event_keywords = models.ManyToManyField(
        PostEventKeyword,
        null=True,
        blank=True,
        help_text='Enter the keyword about event',
        verbose_name='Key words')
    terms_and_condition = models.TextField(
        null=True,
        blank=True,
        help_text='If event has terms and condition \
                   enter atleast 50 characters',
        verbose_name='Terms and Condition')
    event_website = models.CharField(
        max_length=200,
        help_text='Enter the if event has website',
        blank=True,
        null=True)
    is_webinar = models.BooleanField(
        default=False,
        help_text='If its web based events dont consider below content',
        verbose_name='Is web based event?')
    venue = models.TextField(
        null=True,
        blank=True,
        help_text='Enter vanue details',
        verbose_name='Venue')
    country = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Enter Country',
        verbose_name='Country name')
    state = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Enter State ',
        verbose_name='State')
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Enter city ',
        verbose_name='City')
    is_active = models.BooleanField(
        default=False,
        help_text='Enter State ',
        verbose_name='Active')
    is_status = models.BooleanField(
        default=False,
        help_text='For future purpose.Leave as blank ',
        verbose_name='Status')
    admin_status = models.BooleanField(
        default=False,
        help_text='Admin Approval status',
        verbose_name='Admin status')
    payment = models.BooleanField(
        default=False,
        help_text='User paying status',
        verbose_name='Payment status')

    class Meta:
        verbose_name = "Postevent"
        verbose_name_plural = "Postevents"

    def __unicode__(self):
        return self.event_title


class SubCategoryRelatedFieldValue(models.Model):
    postevent = models.ForeignKey(Postevent)
    subcategory_relatedfield = models.ForeignKey(
        SubcategoryRelatedField,
        help_text='Choose subcategory of sub category',
        verbose_name='Choose fields')
    field_value = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='It will be auto loaded.Please select any one field',
        verbose_name='Subcategory of subcategory')

    class Meta:
        verbose_name = "Subcategory Related Field"
        verbose_name_plural = "Subcategory Related Fields"

    def __unicode__(self):
        return self.field_value


class Organizer(models.Model):
    postevent = models.ForeignKey(Postevent)
    organizer_name = models.CharField(
        max_length=50,
        help_text='Enter event organizer name',
        verbose_name='Organizer name')
    organizer_mobile = models.CharField(
        max_length=50,
        help_text='Enter event organizer active mobile number',
        verbose_name='Organizer Mobile')
    organizer_email = models.EmailField(
        max_length=50,
        help_text='Enter event organizer valid email id',
        verbose_name='Organizer Email')

    def __unicode__(self):
        return self.organizer_name
