from django.db import models
from django.conf import settings


class ViberUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    viber_id = models.CharField(max_length=24, unique=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    language = models.CharField(max_length=2, null=True, blank=True)
    device = models.CharField(max_length=24, null=True, blank=True)
    primary_device_os = models.CharField(max_length=128, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    viber_api_version = models.IntegerField(null=True, blank=True)


# Create your models here.
