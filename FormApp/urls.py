from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'), 
    path('',log_in,name='log_in'),

    #For admin:
    #path("index/", index,name='index',)


]