import pprint
import textwrap

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import SearchForm
from pyairtable import Table
from pyairtable.formulas import match, EQUAL, FIELD, to_airtable_value, OR, FIND
import os


# todo: based on tutorial, will have to create objects that
#   represent each search result

def search_result_broad(search_term: str, table: Table) -> list:
    """
    searches for a match in name, transliteration, derivative terms, and
    english translation. (will work in any language).
    """
    # for finding something that has an exact match of name (just one string):
    name_match = EQUAL(FIELD("Name"), to_airtable_value(search_term))

    # for finding transliteration (just one string):
    translit_match = EQUAL(FIELD("Transliteration"), to_airtable_value(search_term))

    # for finding derivative terms (one long string, will contain \n to indicate line breaks):
    deriv_match = FIND(to_airtable_value(search_term), FIELD("Derivative Terms"))

    # for finding in the english translation
    meaning_match = FIND(to_airtable_value(search_term), FIELD("English Translation"))

    # combining to make formula
    formula = OR(name_match, translit_match, deriv_match, meaning_match)

    return table.all(formula=formula)  # returns a list of records, which are themselves dicts


def generate_result(unprocessed: list):
    """
    unprocessed is a list that matches the formatting of records fetched by the AirTable API.
    """
    done = []

    for record in unprocessed:
        new_entry = {'Name': record['fields']['Name'],
                     'English Translation': record['fields']['English Translation'],
                     'Historical Notes': textwrap.shorten(record['fields']['Historical Notes'],
                                                          width=280,
                                                          placeholder="...")
                     }

        done.append(new_entry)

    return done


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            target_table = Table(os.environ["TEMP_KEY"], "appfaeFztiHKrh9DG", "Imported table")

            r = search_result_broad(form.cleaned_data['search_query'], target_table)
            pprint.pp(r)
            r_nice = generate_result(r)

            return render(request, 'search/Search-Result.html', {'form': form, 'results': r_nice})

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
