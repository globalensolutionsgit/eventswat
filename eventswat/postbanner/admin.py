from django.contrib import admin
from postbanner.models import *
import datetime as dt
import datetime
from django import forms


class BannerPlanAdminForm(forms.ModelForm):
    class Meta:
		model = BannerPlan
		fields = "__all__" 

    def clean_page_and_position(self):
        page = self.cleaned_data['page']
        position = self.cleaned_data['position']
        filterargs = { 'page': page, 'position': position }
        if BannerPlan.objects.filter(**filterargs).exists():
            raise forms.ValidationError("This combination already exist.")
        return page,position

class BannerPlanAdmin(admin.ModelAdmin):
    form = BannerPlanAdminForm
    list_display = ('id', 'page','position', 'price', 'plan_duration')


class PostBannerAdmin(admin.ModelAdmin):
	fields=['banner','link', 'pageurl', 'position','startdate','enddate','admin_status','user']
	list_display = ('id', 'banner','link', 'pageurl', 'position', 'bannerplan', 'admin_status')
	list_filter = ['pageurl', 'position']
	search_fields = ['id', 'pageurl','position','bannerplan']    
	list_per_page = 50
	
	def admin_status(self, obj):
		return obj.admin_status 
	admin_status.boolean = False

	def get_readonly_fields(self, request, obj=None):
		if obj: # editing an existing object
			return self.readonly_fields + ('startdate','enddate',)
		return self.readonly_fields

		
# class MainbannerAdmin(admin.ModelAdmin):
# 	fields=['mainbanner','price', 'admin_status']
# 	list_display = ('id', 'mainbanner','price', 'admin_status')
# 	list_filter = ['price', 'admin_status']
# 	search_fields = ['price', 'admin_status']    
# 	list_per_page = 50

# admin.site.register(Mainbanner, MainbannerAdmin)
admin.site.register(PostBanner, PostBannerAdmin)
admin.site.register(BannerPlan, BannerPlanAdmin)
