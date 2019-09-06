from django.contrib import admin
from .models import Service, ServiceType, Order, OrderLine


admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(Order)
admin.site.register(OrderLine)

# Register your models here.
