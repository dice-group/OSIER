"""Table Factory for getting tables."""

import random
import requests
import os

from .table import Table

OSIER_DATA_ENDPOINT = os.environ.get("OSIER_DATA_ENDPOINT", "http://localhost")
TABLE_LIST_URI = OSIER_DATA_ENDPOINT + "/table/list"

def get_table_list():
    r = requests.get(TABLE_LIST_URI)
    r.raise_for_status()
    return r.json()

def get_one_table(offset):
    table_list = get_table_list()
    offset = offset % len(table_list)
    return Table(table_list[offset])

def get_random_table():
    offset = random.randint(0, len(get_table_list()) - 1)
    return get_one_table(offset)
