from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        full_address = request.POST.get('full_address', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        password = request.POST.get('password', '').strip()
        terms = request.POST.get('terms')

        errors = []

        if not full_name or not full_address or not email or not mobile or not password:
            errors.append("All fields are required.")

        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError:
            errors.append("Enter a valid email address.")

        if not mobile.isdigit() or len(mobile) != 10:
            errors.append("Enter a valid 10-digit mobile number.")

        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if not terms:
            errors.append("You must agree to the terms and conditions.")

        if User.objects.filter(email=email).exists():
            errors.append("Email is already registered.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('log_in')

    return render(request, 'FormApp/register.html')


def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')
        if not email or not password:
            messages.error(request, "Please provide both email and password.")
            return redirect('log_in')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email is not registered.")
            return redirect('log_in')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('index')
        else:
            messages.error(request, "Invalid password.")
            return redirect('log_in')

    
    return render(request, 'FormApp/login.html')
