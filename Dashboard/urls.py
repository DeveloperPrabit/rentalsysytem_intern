from django.urls import path
from .admin_views import *
from .views import *

urlpatterns = [
    path("home/", home, name='home'),

    #admin:
    path('users/',view_users, name='view_users'),
    path('users/manage/',manage_user, name='manage_user'),
    path('tenants/',view_tenant, name='view_tenant'),
    path('tenants/manage/',manage_tenant, name='manage_tenant'),
    path('password_change/',change_password, name='change_password',),
    path('view_invoices/', view_invoice, name='view_invoices'),
    path('manage_invoices/', manage_invoices, name='manage_invoices'),
    path("delete/<int:id>",delete_invoices,name='delete_invoices'),
    path('edit_invoice/<int:id>/',edit_invoice, name='edit_invoice'),
    path('users/delete/<int:id>/', delete_user, name='delete_user'),

]