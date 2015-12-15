from datetime import timedelta
from django.contrib import admin
from tracking.models import Visitor, Pageview
from tracking.settings import TRACK_PAGEVIEWS
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404


class VisitorAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'
    list_display = ('session_key', 'user', 'start_time', 'status',
        'pretty_time_on_site', 'ip_address', 'user_agent')
    search_fields = ['user__username', 'ip_address', 'user_agent']
    fieldsets = [
        (None, {'fields':()}), 
        ]

    list_per_page = 100

    def export_csv(modeladmin, request, queryset):
      import csv
      from django.utils.encoding import smart_str
      response = HttpResponse(mimetype='text/csv')
      response['Content-Disposition'] = 'attachment; filename=tracking_visitor.csv'
      writer = csv.writer(response, csv.excel)
      response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
      writer.writerow([
          smart_str(u"ID"),
          smart_str(u"Session_key"),
          smart_str(u"User"),
          smart_str(u"Ip_address"),
          smart_str(u"User_agent"),
          smart_str(u"Start_time"),
          smart_str(u"Expiry_age"),
          smart_str(u"Expiry_time"),
          smart_str(u"Time_on_site"),
          smart_str(u"End_time"),
      ])
      for obj in queryset:
          writer.writerow([
              smart_str(obj.pk),
              smart_str(obj.session_key),
              smart_str(obj.user),
              smart_str(obj.ip_address),
              smart_str(obj.user_agent),
              smart_str(obj.start_time),
              smart_str(obj.expiry_age),
              smart_str(obj.expiry_time),
              smart_str(obj.time_on_site),
              smart_str(obj.end_time),
          ])
      return response
    export_csv.short_description = u"Export CSV"
      
    actions = [export_csv]
    
    
    def __init__(self, *args, **kwargs):
        super(VisitorAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
            
    def has_add_permission(self, request):
        return False

    def status(self, obj):
        if obj.session_ended() or obj.session_expired():
            return 'Offline'
        else: 
            return 'Online'

    def pretty_time_on_site(self, obj):
        if obj.time_on_site is not None:
            return timedelta(seconds=obj.time_on_site)
    pretty_time_on_site.short_description = 'Session time'


admin.site.register(Visitor, VisitorAdmin)


class PageviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'view_time'
    list_display = ('url', 'get_visitor_email', 'ip_address', 'view_time')
    search_fields = ['url', 'visitor__user__email', 'ip_address']
    readonly_fields = ('url', 'actor', 'ip_address', 'view_time')
    fieldsets = [
        (None, {'fields':()}), 
        ]
    
    list_per_page = 100

    def export_csv(modeladmin, request, queryset):
      import csv
      from django.utils.encoding import smart_str
      response = HttpResponse(mimetype='text/csv')
      response['Content-Disposition'] = 'attachment; filename=tracking_pageview.csv'
      writer = csv.writer(response, csv.excel)
      response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
      writer.writerow([
          smart_str(u"ID"),
          smart_str(u"visitor"),
          smart_str(u"url"),
          smart_str(u"view_time"),
          smart_str(u"ip_address"),
          smart_str(u"actor"),
      ])
      for obj in queryset:
          writer.writerow([
              smart_str(obj.pk),
              smart_str(obj.visitor),
              smart_str(obj.url),
              smart_str(obj.view_time),
              smart_str(obj.ip_address),
              smart_str(obj.actor),
          ])
      return response
    export_csv.short_description = u"Export CSV"
      
    actions = [export_csv]
    
    def __init__(self, *args, **kwargs):
        super(PageviewAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
    
    def has_add_permission(self, request):
        return False

    def get_visitor_email(self, instance):
        return instance.visitor.user.email
    get_visitor_email.short_description = 'Actor'

if TRACK_PAGEVIEWS:
    admin.site.register(Pageview, PageviewAdmin)
