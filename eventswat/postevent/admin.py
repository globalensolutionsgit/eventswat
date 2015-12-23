from django.contrib import admin
from postevent.models import *
from events.models import SubcategoryRelatedField
from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from templated_email import send_templated_mail


class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    http://stackoverflow.com/questions/1206903\
    /how-do-i-require-an-inline-in-the-django-admin
    http://stackoverflow.com/questions/16543398/\
    how-do-i-make-a-tabularinline-required-in-django-admin
    """

    def clean(self):
        super(RequiredInlineFormSet, self).clean()
        non_empty_forms = 0
        for form in self:
            if form.cleaned_data:
                non_empty_forms += 1
        if non_empty_forms - len(self.deleted_forms) < 1:
            raise ValidationError("Please fill at least one oraganizer.")


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
    """Must add one Organizer using RequiredInlineFormSet"""
    model = Organizer
    extra = 1
    formset = RequiredInlineFormSet


class SubCategoryRelatedFieldValueInLine(admin.TabularInline):
    model = SubCategoryRelatedFieldValue
    extra = 2
    max_num = 2


class PosteventPosterInline(admin.TabularInline):
    model = PosteventPoster
    extra = 0
    max_num = 4
    exclude = ['event_poster_thumbnil', 'event_poster_medium']


class OrganizerAdmin(admin.ModelAdmin):
    fields = ['postevent', 'organizer_name',
              'organizer_mobile', 'organizer_email']
    list_display = ('postevent', 'organizer_name',
                    'organizer_mobile', 'organizer_email')
    list_filter = ['organizer_name']
    search_fields = ['organizer_name']


class PostEventKeywordAdmin(admin.ModelAdmin):
    fields = ['keyword', 'postevent']
    list_display = ('id', 'keyword')
    search_fields = ['postevent__event_title']


class PosteventAdmin(admin.ModelAdmin):
    fields = ['event_type', 'event_category', 'event_subcategory', 'user_name',
              'user_email', 'user_mobile', 'event_title', 'event_description',
              'event_startdate_time', 'event_enddate_time',
              'terms_and_condition', 'event_website', 'is_webinar', 'venue',
              'country', 'state', 'city', 'is_active', 'admin_status',
              'payment']
    list_display = ('id', 'event_type', 'event_category', 'event_subcategory',
                    'event_title', 'city', 'payment', 'admin_status',)
    list_filter = ['payment', 'admin_status', 'event_subcategory']
    inlines = [PosteventPosterInline,
               SubCategoryRelatedFieldValueInLine, OraganizerInLine]
    list_per_page = 50
    actions = ['send_EMAIL']

    class Media:
        css = {'all': ('css/jquery-ui.css',)}
        js = ('js/jquery.js', 'js/admin.js', 'js/jquery-ui.js')

    def send_EMAIL(self, request, queryset):
        if self.admin_status.boolean:
            print 'admin_status', admin_status
            for i in queryset:
                if i.email:
                    send_templated_mail(
                        template_name='premium_user',
                        subject='Welcome Evewat',
                        from_email='eventswat@gmail.com',
                        recipient_list=[i.user_email],
                        context={
                            'user': i.user_name,
                        },
                    )


class OrganizerAdmin(admin.ModelAdmin):
    fields = ['postevent', 'organizer_name',
              'organizer_mobile', 'organizer_email']
    list_display = ('postevent', 'organizer_name',
                    'organizer_mobile', 'organizer_email')
    list_filter = ['organizer_name']
    search_fields = ['organizer_name']
    list_per_page = 50
    actions = ['send_invitations']

    def send_invitations(self, request, queryset):
        for i in queryset:
            if i.organizer_email:
                send_templated_mail(
                    template_name='welcome',
                    subject="Invitation",
                    from_email='eventswat@gmail.com',
                    recipient_list=[i.organizer_email],
                    context={
                        'user': i.organizer_name,
                    },
                )

admin.site.register(CampusCollege, CampusCollegeAdmin)
admin.site.register(CampusDepartment, CampusDepartmentAdmin)
admin.site.register(Postevent, PosteventAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(PostEventKeyword, PostEventKeywordAdmin)
