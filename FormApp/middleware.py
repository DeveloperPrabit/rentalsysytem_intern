from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect

class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        if user.is_authenticated:
            # Admin should not access user views
            if user.user_type == 'admin':
                if modulename == 'FormApp.home':  # Example user module
                    return redirect(reverse('home'))
            # User should not access admin views
            elif user.user_type == 'user':
                if modulename == 'FormApp.index':  # Example admin module
                    return redirect(reverse('index'))
        else:
            # Redirect unauthenticated users to login unless accessing login/auth pages
            if not (request.path == reverse('login_page') or modulename.startswith('django.contrib.auth')):
                return redirect(reverse('login_page'))