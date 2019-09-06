from django.db import models
from django.conf import settings


class Service(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.service_type.name}'


class Order(models.Model):
    status_CHOICES = [
        (0, 'new'),
        (1, 'ordered'),
        (2, 'deliver'),
        (3, 'canceled')
    ]

    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status_CHOICES, default=0)
    number_order = models.PositiveIntegerField(default=0)


class OrderLine(models.Model):
    quantity = models.PositiveSmallIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class ServiceType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name






# Create your models here.
