# blog/urls.py
from django.urls import path

from theme.views import index


urlpatterns = [
    path('', index),
]
