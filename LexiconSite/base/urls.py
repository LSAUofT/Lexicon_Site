from django.urls import path

from base.views import *

urlpatterns = [
    path('', home, name='home'),  # home page
    path('about/', about, name='about'),  # about page
    path('about/project/', about_project, name='about_project'), # about the project
    path('about/team/', about_team, name='about_team'), # about the team
    path('about/technical-information/', technical_information, name='technical_info'),
    path('contact/', contact, name='contact'),  # contact page
    path('news/', news, name='news'), # news page
]