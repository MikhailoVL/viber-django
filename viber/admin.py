from django.contrib import admin
from viber.models import ViberUser, FAQ, ViberUserStatus


admin.site.register(ViberUserStatus)
admin.site.register(ViberUser)
admin.site.register(FAQ)
# Register your models here.
