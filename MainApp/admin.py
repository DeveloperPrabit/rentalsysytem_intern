from django.contrib import admin
from .models import RentInvoice, Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id','invoice_number', 'tenant', 'date_issued', 'due_date', 'total_amount', 'status']
    search_fields = ['invoice_number', 'tenant__name']
    list_filter = ['status', 'date_issued']
    ordering = ['-date_issued']

admin.site.register(Invoice, InvoiceAdmin)

# RentInvoice Admin
@admin.register(RentInvoice)
class RentInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id','serial_number', 'tenant_name', 'rent_month', 'date', 'total_amount', 'grand_total')
    search_fields = ('serial_number', 'tenant_name', 'rent_month')
    list_filter = ('rent_month',)
    ordering = ('-date',)
