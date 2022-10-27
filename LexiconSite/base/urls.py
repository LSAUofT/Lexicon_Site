from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # for main home page
    path('about/', views.about, name='about'),  # for about page
    path('contact/', views.contact, name='contact'),  # for contact page
]