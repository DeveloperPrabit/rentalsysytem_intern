from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    USER_TYPE = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    username = None  # Remove the username field
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='user')
    address = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=255)
    full_address = models.TextField()
    mobile = models.CharField(max_length=15)
    terms_of_use = models.BooleanField(default=False)  # No need for null=True here.



    USERNAME_FIELD = 'email'  # Email is now the username
    REQUIRED_FIELDS = []  # No extra required fields

    objects = CustomUserManager()  # Use the custom manager

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"


class Admin(models.Model):
    """Model for admin users linked to CustomUser."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin: {self.user.email}"  # Display admin's email in the admin panel
    
