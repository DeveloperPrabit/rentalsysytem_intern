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
    return render(request, 'login.html')


def doLogin(request):
    if request.method != 'POST':
        return redirect(reverse('login_page'))

    # reCAPTCHA validation
    captcha_token = request.POST.get('g-recaptcha-response')
    if not captcha_token:
        messages.error(request, 'Please complete the CAPTCHA')
        return redirect(reverse('login_page'))

    try:
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': captcha_token
            },
            timeout=5
        )
        response.raise_for_status()
        result = response.json()

        if not result.get('success'):
            messages.error(request, 'Invalid CAPTCHA. Please try again.')
            return redirect(reverse('login_page'))

    except requests.exceptions.RequestException as e:
        messages.error(request, 'CAPTCHA verification failed. Please try again.')
        return redirect(reverse('login_page'))

    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        if getattr(user, 'user_type', None) == 'admin':
            return redirect(reverse("home"))
        elif getattr(user, 'user_type', None) == 'manager':
            return redirect(reverse("staff_home"))
        elif getattr(user, 'user_type', None) == 'tenant':
            return redirect(reverse("student_home"))
        return redirect(reverse("home"))
    else:
        messages.error(request, "Invalid email or password")
        return redirect(reverse('login_page'))


def logout_user(request):
    """Logout the user and redirect to login page."""
    logout(request)
    return redirect(reverse('login_page'))


def home(request):
    return render(request,'home.html')
