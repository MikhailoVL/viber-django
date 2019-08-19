from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    ]

    adress = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    is_blocked = models.BooleanField(default=False)

# Create your models here.
