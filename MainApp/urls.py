from django.urls import path
from .views import *


urlpatterns=[
    path("form/",index,name="index"),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('change_password/',change_password, name='change_password'),
    path('change_profile/', view_profile, name='view_profile'),
    path('rental/', add_form, name='add_form'),
    path('tenant_list/', tenant_list, name='tenant_list'),
    path('create-invoice/',create_invoice, name='create_invoice'),
    path('invoices/',invoice_list, name='invoice_list'),
    
]