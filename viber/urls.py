from django.contrib import admin
from django.urls import path, include

from viber.views import callback, set_webhook, unset_webhook, create_faq

urlpatterns = [
    path('callback/', callback),
    path('set/', set_webhook),
    path('unset/', unset_webhook),
    path('form_faq/', create_faq),

]
