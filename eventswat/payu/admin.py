from payu.models import PayuDetails
from django.contrib import admin


class PayuDetailsAdmin(admin.ModelAdmin):
    """Pay data should only readable and cannot modify and add"""
    list_display = ('mihpayid', 'mode', 'status', 'txnid', 'amount',
                    'productinfo', 'bank_code', 'pg_type', 'band_ref_number')
    list_filter = ['status', 'mode']
    search_fields = ['amount', 'bank_code', 'band_ref_number', 'pg_type']
    list_per_page = 50

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('mihpayid', 'mode', 'status',
                                           'txnid', 'key', 'amount',
                                           'discount', 'productinfo',
                                           'error_Message', 'hash_key',
                                           'bank_code', 'pg_type',
                                           'band_ref_number')
        return self.readonly_fields

admin.site.register(PayuDetails, PayuDetailsAdmin)
