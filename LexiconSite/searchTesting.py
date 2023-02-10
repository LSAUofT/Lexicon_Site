"""we're fucking around and finding out!"""
import os
from pprint import pprint

import pyairtable.formulas
from pyairtable import Table
from pyairtable.formulas import match, EQUAL, FIELD, to_airtable_value, OR, FIND
import random, string


# TODO: make the documentation better reflect discoveries made here

# TODO: fix the authentication key
# NOTE: my local code had a personal access token as a global variable here, you will have to generate your own
#   following the instructions on Notion, then add it to your environment variables

# NOTE: function for getting the search term from user input [being worked on in search app]

# todo: build a filtering function?? -- inside a given tag, filter based on language? -- airtable should have
#  internal filters


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

    return table.all(formula=formula)



def search_result_narrow(search_term: str, table: Table) -> str:
    """
    This function will take a search term, query the airtable API,
    return a list containing string representation(s) of the record(s) that
    has that search term as a name.
    """
    # build formula based on search term
    # this will be a VERY rudimentary search (will only search the name of the term, looking for exact match)
    formula = match({"Name": search_term}, match_any=True)

    # list of records that have the desired name
    results = table.all(formula=formula)

    return results

unique_ids = set()

def generate_id():
    new_id = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    while new_id in unique_ids:
        new_id = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return new_id

def download_images(search_result: list):
    """
    search_results is assumed to be in the form of a list returned by pyairtable's search function
    """
    # TODO: create function for images
    # print statements for testing
    import requests
    image_list = search_result[0]['fields']['Images']
    for item in image_list:
        print(item)
        image_url = item['url']
        img_data = requests.get(image_url).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)
            # figure out how to save in static
            # figure out how to rewrite the name



if __name__ == '__main__':
    # building table: args are personal access token, base id, and table name
    target_table = Table(os.environ["TEMP_KEY"], "appfaeFztiHKrh9DG", "Imported table")
    download_images(search_result_broad("shengtai", target_table))

    # print statements for testing
    print(search_result_narrow("民族", target_table))
    print(search_result_broad("生態學", target_table))
    print(search_result_broad("shengtai", target_table))
    print(search_result_broad("生態學家", target_table))