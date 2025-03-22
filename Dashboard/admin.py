from django.contrib import admin
from .models import CustomUser, Admin

# Custom User Admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

# Register Admin model
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin',)

admin.site.register(Admin, AdminAdmin)
