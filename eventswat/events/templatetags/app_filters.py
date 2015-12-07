from django import template
from django.db.models import *
from postbanner.models import *
from events.views import *
from events.models import *
from postevent.models import Postevent
from eventswat.util import *
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
def get_main_banner(banner):
	banner=PostBanner.objects.all()
	return banner

@register.filter
def get_banner(banner):
	banner=PostBanner.objects.all()
	return banner
	
@register.filter
def get_categories(initial_load):  
	category=EventsCategory.objects.all().order_by('id')	
	return category

@register.filter
def get_subcategories(categoryId):  	
	print "get_subcategories"
	subcategories = EventsSubCategory.objects.filter(category__id=categoryId)		
	print "subcategories", subcategories
	return subcategories	

@register.filter
def get_photos(photo): 
	photo=str(photo).split(',')
	return photo[0]

@register.filter
@stringfilter
def get_subcategoriesCount(subCategoryId, categoryId):
    subcategoriescounts = Postevent.objects.filter(event_category_id=categoryId,event_subcategory_id=subCategoryId, admin_status=1).count()
    return subcategoriescounts
