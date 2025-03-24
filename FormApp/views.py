from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.http import HttpResponse
from .EmailBackend import EmailBackend


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        full_address = request.POST.get('full_address', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        password = request.POST.get('password', '').strip()
        terms = request.POST.get('terms') == 'on'  # Handle checkbox value correctly

        errors = []
        # Google reCAPTCHA
        captcha_token = request.POST.get('g-recaptcha-response')
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_key = "6LfswtgZAAAAABX9gbLqe-d97qE2g1JP8oUYritJ"
        data = {
            'secret': captcha_key,
            'response': captcha_token
        }

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
        
        # Create the user
        user =User.objects.create(
            full_name=full_name,
            full_address=full_address,
            email=email,
            mobile=mobile,
            password=password,
            terms_of_use=terms,  # Set terms_of_use value
        )

        user.first_name = full_name
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login_page')

    return render(request, 'FormApp/register.html')





def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")

    # Assuming EmailBackend is a custom backend, make sure it's imported properly
    user = EmailBackend().authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

    if user is not None:
        # Login the user
        login(request, user)
        
        # Redirect user based on user type
        if user.user_type == 'admin':  # Correctly checking user_type field
            return redirect(reverse("home"))
        elif user.user_type == 'user':  # Correctly checking user_type field
            return redirect(reverse("index"))
        else:
            messages.error(request, "Invalid user type.")
            return redirect("login_page")
    else:
        messages.error(request, "Invalid login credentials.")
        return redirect("login_page")


def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'admin':  # Correctly checking user_type field
            return redirect(reverse("home"))
        elif request.user.user_type == 'user':  # Correctly checking user_type field
            return redirect(reverse("index"))
    return render(request, 'FormApp/login.html')


def Logout_view(request):
    logout(request)
    return redirect('login_page')