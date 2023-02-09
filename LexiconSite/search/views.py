import pprint

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import SearchForm
from pyairtable import Table
from pyairtable.formulas import match, EQUAL, FIELD, to_airtable_value, OR, FIND
import os


# todo: based on tutorial, will have to create objects that
#   represent each search result

def search_result_broad(search_term: str, table: Table) -> str:
    """
    searches for a match in name, transliteration, and derivative terms. (will work in any language).
    """
    # for finding something that has an exact match of name (just one string):
    name_match = EQUAL(FIELD("Name"), to_airtable_value(search_term))

    # for finding transliteration (just one string):
    translit_match = EQUAL(FIELD("Transliteration"), to_airtable_value(search_term))

    # for finding derivative terms (one long string, will contain \n to indicate line breaks):
    deriv_match = FIND(to_airtable_value(search_term), FIELD("Derivative Terms"))

    # combining to make formula
    formula = OR(name_match, translit_match, deriv_match)

    return table.all(formula=formula)  # returns a list of records, which are themselves dicts


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            target_table = Table(os.environ["TEMP_KEY"], "appfaeFztiHKrh9DG", "Imported table")

            r = search_result_broad(form.cleaned_data['search_query'], target_table)
            pprint.pp(r)

            # have temporarily made this "Search-Results.html" (note the plural) to test result finding
            return render(request, 'search/Search-Results.html', {'form': form, 'results': r})

    else:
        form = SearchForm()

    return render(request, 'search/Search.html', {'form': form})


def advanced_search(request):
    return render(request, 'search/Advanced-Search.html')


def search_results(request):
    return render(request, 'search/Search-Result.html')


class SearchHomeView(TemplateView):
    template_name = 'search/Search-Home.html'


class SearchResultView(ListView):  # notes: object_list is the default name for the context object ListView returns
    template_name = 'search/Search-Results.html'

    def get_queryset(self):  # todo: figure out how to connect pyairtable search functions
        query = self.request.GET.get("q")  # from QueryDict, gets item corresponding to key 'q'
        object_list = [num for num in range(1,
                                            len(query) + 1)]  # this will display "results" a number of times equal to number of chars in search query
        return object_list
