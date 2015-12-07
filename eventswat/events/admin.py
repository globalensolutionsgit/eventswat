from django.contrib import admin
from events.models import *


class EventsCategoryAdmin(admin.ModelAdmin):
	fields=['category_name']
	list_display = ('id', 'category_name')
	list_filter = ['category_name']
	search_fields = ['id', 'category_name']    
	list_per_page = 50

class EventsSubCategoryAdmin(admin.ModelAdmin):
	fields=['subcategory_name', 'subcategory_icon', 'category','subcategory_hover_icon']
	list_display = ('id','subcategory_name','subcategory_icon','subcategory_hover_icon')
	list_filter = ['subcategory_name']
	search_fields = ['id', 'subcategory_name']
	list_per_page = 50

class CityAdmin(admin.ModelAdmin):
	fields=['city','state']
	list_display = ('id', 'city','state')
	list_filter = ['city']
	search_fields = ['id', 'city']
	list_per_page = 50

# class PremiumPriceInfoAdmin(admin.ModelAdmin):
# 	fields=['premium_price','currency','purpose','month']
# 	list_display = ('premium_price','currency','purpose','month')
# 	list_filter = ['currency']
# 	search_fields = ['id', 'currency']
# 	list_per_page = 50


admin.site.register(EventsCategory, EventsCategoryAdmin)
admin.site.register(City, CityAdmin)
# admin.site.register(PremiumPriceInfo, PremiumPriceInfoAdmin) 
admin.site.register(EventsSubCategory, EventsSubCategoryAdmin)
# admin.site.register(CollegeDepartment) 


