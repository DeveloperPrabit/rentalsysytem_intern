from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
import requests

def login_page(request):
    """Render the login page if the user is not authenticated."""
    if request.user.is_authenticated:
        if getattr(request.user, 'user_type', None) == 'admin':
            return redirect(reverse("home"))
        elif getattr(request.user, 'user_type', None) == 'manager':
            return redirect(reverse("staff_home"))
        elif getattr(request.user, 'user_type', None) == 'tenant':
            return redirect(reverse("student_home"))
    return render(request, 'Dashboard/login.html')


def doLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            messages.error(request, "Invalid email or password")
            return redirect("doLogin")
    
    return render(request, "Dashboard/login.html")
    

def logout_user(request):
    """Logout the user and redirect to login page."""
    logout(request)
    return redirect(reverse('login_page'))


def home(request):
    return render(request,'Dashboard/home.html')


