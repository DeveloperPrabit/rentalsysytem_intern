from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'), 
    path('',login_page,name='login_page'),
    path('dologin/',doLogin, name='doLogin'),
    path('accounts/logout/', Logout_view, name='logout'),

    #path('admin/logout/',admin_logout, name='admin_logout'), 
 
]