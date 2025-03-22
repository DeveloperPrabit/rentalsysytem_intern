from django.db import models


# Create your models here.

class CustomUser(models.Model):
    full_name = models.CharField(max_length=255)
    full_address = models.TextField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    terms_of_use = models.BooleanField(default=False)
    is_not_robert = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

from django.contrib.auth.models import AbstractUser

