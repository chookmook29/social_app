from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='', default='default.jpg')
    approved = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)
    dob = models.DateField(default='1901-01-01')
