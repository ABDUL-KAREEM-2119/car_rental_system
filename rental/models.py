from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class User(AbstractUser):
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role.role_name if self.role else 'No Role'})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    car_type = models.CharField(max_length=100)
    year = models.IntegerField()
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image_url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class ContactDetail(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"Contact Detail {self.email}"
