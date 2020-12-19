"""
Definition of urls for FinalPython.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path, include


urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),      
        ]
