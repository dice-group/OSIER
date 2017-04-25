"""Table Factory for getting tables."""

import random
import requests
import os
import msgpack

from osier.table import Table
from osier.pathes import ATOMIC_TABLES_DIR

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

def load_atomic_tables():
    atomic_tables = []
    atomic_table_ids = []
    file_list = os.listdir(ATOMIC_TABLES_DIR)
    for _filename in file_list:
        if _filename.endswith(".table"):
            filepath = os.path.join(ATOMIC_TABLES_DIR, _filename)
            _id = _filename.split(".")[0]
            _f = open(filepath, "rb")
            atomic_table = msgpack.unpackb(_f.read())
            _f.close()
            atomic_table_ids.append(_id)
            atomic_tables.append(atomic_table)
    return (atomic_table_ids, atomic_tables)
