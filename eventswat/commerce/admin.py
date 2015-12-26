from django.contrib import admin
from commerce.models import Order, Transaction


class OrderAdmin(admin.ModelAdmin):
    fields = ['banner', 'banner_plan']
    list_display = ('id', 'banner_name', 'banner_plan_page',)
    list_filter = ['banner__admin_status', 'banner_plan__page','banner_plan__position']
    search_fields = ['banner__user']
    list_per_page = 50

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('banner', 'banner_plan')
        return self.readonly_fields

    def banner_name(self, obj):
        return obj.banner.user
    banner_name.short_description = 'User'

    def banner_plan_page(self, obj):
        return obj.banner_plan.page
    banner_plan_page.short_description = 'Page'

class TransactionAdmin(admin.ModelAdmin):
    fields = ['user', 'transaction_mode', 'post_type', 'order', 'payu', 'account_no',]
    list_display = ('id', 'user', 'transaction_mode', 'post_type', 'order_id', 'payu' , 'admin_status')
    list_filter = ['transaction_mode', 'post_type']
    search_fields = ['user__username', 'order', 'payu__mihpayid']
    list_per_page = 50

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user', 'transaction_mode', 'post_type', 'order', 'payu')
        return self.readonly_fields

    def order_id(self, obj):
        return obj.order.banner_plan
    order_id.short_description = 'Order Number'

    def admin_status(self, obj):
        return obj.order.banner.admin_status
    admin_status.short_description = 'Admin Approval of banner'



admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction, TransactionAdmin)
