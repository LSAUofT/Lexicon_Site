"""we're fucking around and finding out!"""
import os

from pyairtable import Table
from pyairtable.formulas import match

# TODO: make the documentation reflect discoveries made here
# NOTE: gives everything in the form of a nested dictionary

# NOTE: my local code had a personal access token as a global variable here, you will have to generate your own
#   following the instructions on Notion

# TODO: function for getting the search term?


def search_result(search_term: str, table: Table) -> str:
    """write a function that will take a search term, query the airtable API,
    return a list of all the items with the"""
    # note: how are you then going to display the results??
    # going to need an OAuth access token -- i think for the time being we only need the data.records:read scope
    # try using the OAuth token just in place of the API key?
    # assume somewhere that you've grabbed the airtable API key, need a separate function to build the table
    # here, build formula based on search term
    # then, return list of results for displaying to front end??
    # note that you then also will have to include pyairtable in the requirements.txt
    # this will be a VERY rudimentary search (will only search the name of the term, looking for exact match, but:
    # i don't know how the search will work with the tags
    formula = match({"Name": search_term}, match_any=True)  # title will be whatever the name of the card is -- check air table for name -- could do with multiple columns?

    # questions for everyone else: how are we doing the search bar?

    results = table.all(formula=formula)

    return results

if __name__ == '__main__':
    table = Table(TEST_KEY, "appfaeFztiHKrh9DG", "Imported table")  # TEST_KEY is the removed personal access token
    result = search_result("心理學", table)
    print(result)
    if "心理學" in result[0]['fields']['Description']:
        print("yes")
    else:
        print("no")

