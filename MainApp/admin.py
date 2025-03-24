from django.contrib import admin
from .models import Tenant,RentInvoice
#create your admin page:


class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile', 'email', 'house_name', 'flat_number', 'room_number', 'rent_amount', 'rent_start_date']

admin.site.register(Tenant, TenantAdmin)

@admin.register(RentInvoice)
class RentInvoiceAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'tenant_name', 'rent_month', 'date', 'total_amount', 'grand_total')
    search_fields = ('serial_number', 'tenant_name', 'rent_month')
    list_filter = ('rent_month',)
    ordering = ('-date',)
