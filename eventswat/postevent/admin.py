from django.contrib import admin
from postevent.models import *
from events.models import SubcategoryRelatedField
from django import forms
from flexselect import FlexSelectWidget


class CampusCollegeAdmin(admin.ModelAdmin):
    fields = ['college_name', 'city']
    list_display = ('id', 'college_name', 'city',)
    list_filter = ['city__state']
    search_fields = ['id', 'college_name']
    list_per_page = 50


class CampusDepartmentAdmin(admin.ModelAdmin):
    fields = ['department', 'college']
    list_display = ('id', 'department')
    search_fields = ['id', 'department']
    list_per_page = 50


class OraganizerInLine(admin.TabularInline):
    model = Organizer
    extra = 0

class SubCategoryRelatedFieldValueInLine(admin.TabularInline):
    model = SubCategoryRelatedFieldValue
    extra = 0


# class SubCategorywidget(FlexSelectWidget):
#     """
#     The widget must extend FlexSelectWidget and implement trigger_fields,
#     details(), queryset() and empty_choices_text().
#     """
#
#     trigger_fields = ['event_category']
#     """Fields which on change will update the base field."""
#
#     def queryset(self, instance):
#         """
#         Returns the QuerySet populating the base field. If either of the
#         trigger_fields is None, this function will not be called.
#
#         - instance: A partial instance of the parent model loaded from the
#                     request.
#         """
#         print 'install',instance
#         company = instance.eventscategory.category_name
#         return EventsSubCategory.objects.filter(category=company)
#
#     def empty_choices_text(self, instance):
#         """
#         If either of the trigger_fields is None this function will be called
#         to get the text for the empty choice in the select box of the base
#         field.
#
#         - instance: A partial instance of the parent model loaded from the
#                     request.
#         """
#         return "  ----------             "


class PosteventAdmin(admin.ModelAdmin):

    filelds = ['event_type', 'event_category', 'event_subcategory']
    list_display = ('id', 'event_type', 'event_category', 'event_subcategory')
    inlines = [ SubCategoryRelatedFieldValueInLine, OraganizerInLine ]

    class Media:
        js = ('js/jquery.js', 'js/admin.js' )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    # 	"""Alters the widget displayed for the base field."""
    #     if db_field.name == "event_subcategory":
	#         kwargs['widget'] = SubCategorywidget(
	#             base_field=db_field,
	#             modeladmin=self,
	#             request=request,
	#         )
	#         kwargs['label'] = 'Event subcategory'
    #     return super(PosteventAdmin, self).formfield_for_foreignkey(db_field,request, **kwargs)
    # actions = ['send_EMAIL']
    # inlines = [ OraganizerInLine ]

    # def admin_status(self, obj):
    # 	return obj.admin_status
    # admin_status.boolean = False

# 	def send_EMAIL(self,request, queryset):
# 		from templated_email import send_templated_mail
# 		if self.admin_status.boolean == True :
# 			print 'admin_status', admin_status
# 			for i in queryset:
# 				if i.email:
# 					send_templated_mail(
# 							template_name = 'premium_user',
# 				            subject = 'Welcome Evewat',
# 				            from_email = 'eventswat@gmail.com',
# 				            recipient_list = [i.email],
# 				            context={
# 				                       'user': i.name,
# 				                    },
# 				        )

# 	def get_readonly_fields(self, request, obj=None):
# 		if obj: # editing an existing object
# 			return self.readonly_fields + ('payment',)
# 		return self.readonly_fields

# class OrganizerAdmin(admin.ModelAdmin):
# 	fields = ['postevent','organizer_name','organizer_mobile','organizer_email']
# 	list_display = ('postevent','organizer_name','organizer_mobile','organizer_email')
# 	list_filter = ['organizer_name']
# 	search_fields = ['organizer_name']
# 	list_per_page = 50
# 	actions = ['send_invitations']

# 	def send_invitations(self, request, queryset):
# 		from templated_email import send_templated_mail
# 		for i in queryset:
# 			if i.organizer_email:
# 				send_templated_mail(
# 						template_name = 'welcome',
# 			            subject = "Invitation",
# 			            from_email = 'eventswat@gmail.com',
# 			            recipient_list = [i.organizer_email],
# 			            context={
# 			                       'user': i.organizer_name,
# 			                    },
admin.site.register(CampusCollege, CampusCollegeAdmin)
admin.site.register(CampusDepartment, CampusDepartmentAdmin)
admin.site.register(Postevent, PosteventAdmin)
# admin.site.register(Organizer,OrganizerAdmin)
