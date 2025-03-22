from django.urls import path
from .views import doLogin, login_page, logout_user, home

urlpatterns = [
    path("login/", login_page, name='login_page'),
    path("doLogin/", doLogin, name='doLogin'),
    path("logout/", logout_user, name='logout_user'),
    path("home/", home, name='home'),
]
