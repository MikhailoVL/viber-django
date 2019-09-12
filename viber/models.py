from django.db import models
from django.conf import settings
from .managers import ViberUserStatusManager



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
    is_blocked = models.BooleanField(default=False)



class FAQ(models.Model):

    question = models.CharField(max_length=128, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question
# Create your models here.


class ViberUserStatus(models.Model):
    STATUSES = [
        (-1, "default"),
        (0, "subscribed"),
        (1, "unsubscribed"),
        (2, "getfone"),

    ]
    viber_user = models.ForeignKey(ViberUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUSES, default=0)

    objects = ViberUserStatusManager()
