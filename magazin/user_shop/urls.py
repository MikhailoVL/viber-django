from django.contrib import admin
from django.urls import path, include

from user_shop.views import callback

urlpatterns = [
    path('callback/', callback)

    ]