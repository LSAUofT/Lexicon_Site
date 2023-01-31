from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# todo: based on tutorial, will have to create objects that
#   represent each search result

def search(request):
    return render(request, 'search/Search.html')


def advanced_search(request):
    return render(request, 'search/Advanced-Search.html')


class SearchHomeView(TemplateView):
    template_name = 'search/Search-Home.html'


class SearchResultView(ListView):  # notes: object_list is the default name for the context object ListView returns
    template_name = 'search/Search-Results.html'

    def get_queryset(self):  # todo: figure out how to connect pyairtable search functions
        query = self.request.GET.get("q")   # from QueryDict, gets item corresponding to key 'q'
        object_list = [num for num in range(1, len(query) + 1)]    # this will display "results" a number of times equal to number of chars in search query
        return object_list
