from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Tenant(models.Model):
    photo = models.ImageField(upload_to='tenant_photos/', null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    profession = models.CharField(max_length=100, null=True, blank=True)
    house_name = models.CharField(max_length=100, default='Unknown')  # Provide a default value here
    flat_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rent_start_date = models.DateField()

    def __str__(self):
        return self.name 
    

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='invoices')
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Overdue', 'Overdue')], default='Unpaid')

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.tenant.name}"
