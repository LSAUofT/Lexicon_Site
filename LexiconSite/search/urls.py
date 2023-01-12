from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('search/', search, name='search'),  # initial search page
]