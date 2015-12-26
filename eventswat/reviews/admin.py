from django.contrib import admin
from reviews.models import *

class WebsiteFeedbackAdmin(admin.ModelAdmin):
	fields=['name','email','comments',]
	list_display = ('name','email','comments',)
	list_filter = ['name']
	search_fields = ['id', 'name']
	list_per_page = 50

admin.site.register(WebsiteFeedback, WebsiteFeedbackAdmin)
admin.site.register(Comment)
