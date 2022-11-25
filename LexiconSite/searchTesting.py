"""we're fucking around and finding out!"""
import os

from pyairtable import Table
from pyairtable.formulas import match

# TODO: make the documentation reflect discoveries made here
# NOTE: my local code had a personal access token as a global variable here, you will have to generate your own
#   following the instructions on Notion

# TODO: function for getting the search term?

# TODO: multiple types of search? (searching just name, searching through tags and text body and name? etc?)

# TODO: a separate function to build the table? (see if statement below)


def search_result(search_term: str, table: Table) -> str:
    """write a function that will take a search term, query the airtable API,
    return a list of all the items with the same term"""
    # build formula based on search term
    # this will be a VERY rudimentary search (will only search the name of the term, looking for exact match)
    formula = match({"Name": search_term}, match_any=True)

    # list of records that have the desired name
    results = table.all(formula=formula)

    return results

if __name__ == '__main__':
    # building table: TEST_KEY is the removed personal access token, the second arg is base idea for test base,
    #   third arg is the name of the table we want to look at
    table = Table(TEST_KEY, "appfaeFztiHKrh9DG", "Imported table")
    result = search_result("心理學", table)
    print(result)
    if "心理學" in result[0]['fields']['Description']:
        print("yes")
    else:
        print("no")

