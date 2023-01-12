from django.contrib import admin
from django.urls import path, include
from .views import SearchHomeView, SearchResultView

urlpatterns = [
    # path('search/', SearchHomeView.as_view(), name='search_home'),  # initial search page
    path('', SearchHomeView.as_view(), name='search_home'), # for testing, so it doesn't need to connect to other app yet
    path('search/results/', SearchResultView.as_view(), name='search_results')  # search results page
]