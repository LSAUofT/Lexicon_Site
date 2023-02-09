from django.contrib import admin
from django.urls import path, include
from .views import SearchHomeView, SearchResultView, search, advanced_search, search_results

urlpatterns = [
    # path('search/', SearchHomeView.as_view(), name='search_home'),  # initial search page
    # path('', SearchHomeView.as_view(), name='search_home'), # for testing, so it doesn't need to connect to other app yet
    path('search/', search, name='search'),
    # path('search/results/', SearchResultView.as_view(), name='search_results')  # search results page
    path('search/advanced', advanced_search, name='advanced_search'),
    path('search/results', search_results, name='search_results')
]