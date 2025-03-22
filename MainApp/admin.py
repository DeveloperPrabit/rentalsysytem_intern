from django.contrib import admin
from .models import Tenant
#create your admin page:


class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile', 'email', 'house_name', 'flat_number', 'room_number', 'rent_amount', 'rent_start_date']

admin.site.register(Tenant, TenantAdmin)



