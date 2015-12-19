from django.contrib import admin

from models import ErrorLog

class ErrorLogAdmin(admin.ModelAdmin):
    ordering = ('-datetime',)
    list_display = ('level', 'error_msg', 'page', 'datetime', 'ip_address', 'user', 'admin_status')
    list_filter = ('level', 'admin_status')
    search_fields = ('level','error_msg', 'user', 'page', 'admin_status', 'ip_address', 'page')
    date_hierarchy = 'datetime'
    
    list_per_page = 100

    def export_csv(modeladmin, request, queryset):
      import csv
      from django.utils.encoding import smart_str
      response = HttpResponse(mimetype='text/csv')
      response['Content-Disposition'] = 'attachment; filename=errorlog.csv'
      writer = csv.writer(response, csv.excel)
      response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
      writer.writerow([
          smart_str(u"ID"),
          smart_str(u"Level"),
          smart_str(u"Error_msg"),
          smart_str(u"Page"),
          smart_str(u"Ip_address"),
          smart_str(u"User"),
          smart_str(u"Datetime"),
          smart_str(u"Admin_status"),
          smart_str(u"Admin_note"),
          smart_str(u"Admin_note_created"),
          smart_str(u"Admin_note_modified"),
      ])
      for obj in queryset:
          writer.writerow([
              smart_str(obj.pk),
              smart_str(obj.level),
              smart_str(obj.error_msg),
              smart_str(obj.page),
              smart_str(obj.ip_address),
              smart_str(obj.user),
              smart_str(obj.datetime),
              smart_str(obj.admin_status),
              smart_str(obj.admin_note),
              smart_str(obj.admin_note_created),
              smart_str(obj.admin_note_modified),
          ])
      return response
    export_csv.short_description = u"Export CSV"
      
    actions = [export_csv]
    
    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('level', 'error_msg', 'page', 'datetime', 'ip_address', 'user')

admin.site.register(ErrorLog, ErrorLogAdmin)