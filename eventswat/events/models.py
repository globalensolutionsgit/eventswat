from django.db import models
from PIL import Image


class DateAbstract(models.Model):
    """This is common for requried model"""
    created_date = models.DateTimeField(max_length=50, auto_now_add=True)
    modified_date = models.DateTimeField(max_length=50, auto_now=True)

    class Meta:
        abstract = True


class EventsCategory(models.Model):
    """
    This model for list of categories,icon path and hover_icon paths.
    Icons stored to media folders.
    """
    category_name = models.CharField(
        max_length=150,
        unique=True,
        help_text='Enter category name without space.',
        verbose_name="Name of category")
    category_icon = models.ImageField(
        upload_to='category/icon/',
        max_length=100,
        default='',
        help_text='Upload icon image as .jpg or .png',
        verbose_name="Icon")
    category_hover_icon = models.ImageField(
        upload_to='category/icon/',
        max_length=100, default='',
        help_text='Upload hover icon imageas as .jpg or .png \
        (This icon show when mouse over icon)',
        verbose_name="Hover Icon")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __unicode__(self):
        return self.category_name


class EventsSubCategory(models.Model):
    """
    This model store the subcategory for multiple categories.
        Icons stores into media folders
    """
    category = models.ManyToManyField(
        EventsCategory,
        help_text='Select which categories has this subcategory.',
        verbose_name='Category List')
    subcategory_name = models.CharField(
        max_length=50,
        help_text='Enter subcategory name without space.',
        verbose_name="Name of subcategory")
    subcategory_icon = models.ImageField(
        upload_to='subcategory/icon/',
        max_length=100,
        help_text='Upload icon image as .jpg or .png',
        verbose_name="Subcategory Icon", null=True, blank=True)
    subcategory_hover_icon = models.ImageField(
        upload_to='subcategory/icon/',
        max_length=100,
        help_text='Upload hover icon imageas as .jpg or .png \
        (This icon show when mouse over icon)',
        verbose_name="Subcategory Hover Icon", null=True, blank=True)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        ordering = ['id']

    def __unicode__(self):
        return self.subcategory_name


class SubcategoryRelatedField(models.Model):
    """This model for if we need to specify from one Subcategory"""
    field_name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Enter the subcategory of subcategory name.',
        verbose_name="Name of Field")
    related_subcategory = models.ManyToManyField(
        EventsSubCategory,
        help_text='Select which categories has this field name.',
        verbose_name="Subcategory")

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.field_name


class City(models.Model):
    """Store the information about list cites"""
    city = models.CharField(
        max_length=150,
        help_text='Enter city name.',
        verbose_name="Name of city",)
    state = models.CharField(
        max_length=100,
        default='',
        help_text='Enter state name.',
        verbose_name="Name of state",)
    country_code = models.CharField(
        max_length=10,
        null=True,
        help_text='Enter Country code.',
        verbose_name="Code of Country",)
    country_name = models.CharField(
        max_length=50,
        null=True,
        help_text='Enter country name.',
        verbose_name="Name of country",)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ['id']
        unique_together = ('city', 'state', 'country_code', 'country_name')

    def __unicode__(self):
        return self.city
