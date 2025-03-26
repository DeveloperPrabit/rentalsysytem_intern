from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings



class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Helper function to create users with hashed passwords."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hashes password
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if not extra_fields.get("terms_of_use", False):
            raise ValueError("Users must accept the Terms of Use.")
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    user_type = [
        ('admin', 'admin'),
        ('user', 'user'),
    ]

    username = None  # Remove username field
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)  # Ensure unique mobile numbers
    user_type = models.CharField(max_length=10, choices=user_type, default='user')
    terms_of_use = models.BooleanField(default=False)  # Required during registration
    full_name = models.CharField(max_length=255)
    full_address = models.TextField()
    USERNAME_FIELD = 'email'  # Set email as the username
    REQUIRED_FIELDS = []  # Essential fields

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} ({self.get_user_type_display()})"



class Admin(models.Model):
    """Model for admin users linked to CustomUser."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin: {self.user.email}"  # Display admin's email in the admin panel
    
