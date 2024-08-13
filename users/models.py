from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    license_number = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username
