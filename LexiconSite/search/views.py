from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# todo: based on tutorial, will have to create objects that
#   represent each search result

class SearchHomeView(TemplateView):
    template_name = 'search/Search-Home.html'


class SearchResultView(ListView):  # notes: object_list is the default name for the context object ListView returns
    template_name = 'search/Search-Results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = [1, 2, 3]    # this is placeholder at the moment, can connect to search function later
        return object_list
