import os
import requests

from osier.tablefactory import get_table_list

OSIER_DATA_ENDPOINT = os.environ.get("OSIER_DATA_ENDPOINT", "http://localhost")
TRIPLES_URI = OSIER_DATA_ENDPOINT + "/triples/{}.nt"

def get_all_triples():
    table_list = get_table_list()
    all_triples = ""
    for table_id in table_list:
        triples = get_triples_for_table_id(table_id)
        all_triples += triples
    return all_triples

def get_triples_for_table_id(table_id):
    r = requests.get(TRIPLES_URI.format(table_id))
    r.raise_for_status()
    return r.content.decode("utf-8")
