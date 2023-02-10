from django.urls import path

from base.views import *

urlpatterns = [
    path('', home, name='home'),  # home page
    # path('home/', home, name='home'),   # for testing the search app without connecting the two
    path('about/', about, name='about'),  # about page
    path('about/project/', about_project, name='about_project'), # about the project
    path('about/team/', about_team, name='about_team'), # about the team
    path('about/technical-information/', technical_information, name='technical_info'),
    path('contact/', contact, name='contact'),  # contact page
    path('contact/thanks/', thanks, name='thanks'),  # thanks page, testing
    path('news/', news, name='news'),  # news page
    path('lexicon/', lexicon, name='lexicon')  # for testing, the lexicon page
]