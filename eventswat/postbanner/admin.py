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
        filterargs = {'page': page, 'position': position}
        if BannerPlan.objects.filter(**filterargs).exists():
            raise forms.ValidationError("This combination already exist.")
        return page, position


class BannerPlanAdmin(admin.ModelAdmin):
    form = BannerPlanAdminForm
    list_display = ('id', 'page', 'position', 'price', 'plan_duration')


class PostBannerAdmin(admin.ModelAdmin):
    fields = ['user', 'bannerplan', 'banner', 'link',
              'startdate', 'enddate', 'admin_status']
    list_display = ('id', 'banner', 'link', 'admin_status')
    list_filter = ['user', 'banner']
    search_fields = ['id', 'banner']
    list_per_page = 50

    def admin_status(self, obj):
        return obj.admin_status
    admin_status.boolean = False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('startdate', 'enddate',)
        return self.readonly_fields


class TempBannerAdmin(admin.ModelAdmin):
    fields = ['temp_user', 'temp_bannerplan', 'temp_banner',
              'temp_link', 'temp_startdate', 'temp_enddate']
    list_display = ('id', 'temp_banner', 'temp_link')
    list_filter = ['temp_user', 'temp_banner']
    search_fields = ['id', 'temp_banner']
    list_per_page = 50

admin.site.register(PostBanner, PostBannerAdmin)
admin.site.register(BannerPlan, BannerPlanAdmin)
admin.site.register(TempBanner, TempBannerAdmin)
