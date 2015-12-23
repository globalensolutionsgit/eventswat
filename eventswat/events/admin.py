from django.contrib import admin
from events.models import (EventsCategory, EventsSubCategory,
                           SubcategoryRelatedField, City)


class EventsCategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'category_icon', 'category_hover_icon']
    list_display = ('id', 'category_name',
                    'category_icon', 'category_hover_icon')
    search_fields = ['category_name']
    list_per_page = 20


class EventsSubCategoryAdmin(admin.ModelAdmin):
    fields = ['subcategory_name', 'category',
              'subcategory_icon', 'subcategory_hover_icon']
    list_display = ('id', 'subcategory_name',
                    'subcategory_icon', 'subcategory_hover_icon')
    list_filter = ['category']
    search_fields = ['id', 'subcategory_name']
    list_per_page = 50


class SubcategoryRelatedFieldAdmin(admin.ModelAdmin):
    fields = ['field_name', 'related_subcategory']
    list_display = ('id', 'field_name')
    list_filter = ['field_name']
    search_fields = ['field_name']
    list_per_page = 30


class CityAdmin(admin.ModelAdmin):
    fields = ['city', 'state', 'country_code', 'country_name']
    list_display = ('id', 'city', 'state', 'country_code', 'country_name')
    list_filter = ['country_name', 'state']
    search_fields = ['id', 'city', 'state', 'country_name']
    list_per_page = 50

admin.site.register(EventsCategory, EventsCategoryAdmin)
admin.site.register(EventsSubCategory, EventsSubCategoryAdmin)
admin.site.register(SubcategoryRelatedField, SubcategoryRelatedFieldAdmin)
admin.site.register(City, CityAdmin)
