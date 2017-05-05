"""Table Factory for getting tables."""

import random
import requests
import os
import msgpack
import subprocess
import pickle

from osier.table import Table
from osier.pathes import ATOMIC_TABLES_DIR, ATOMIC_TABLES_INDEX, \
    ATOMIC_TABLES_TOP_HASHES_SIMPLE, ATOMIC_TABLES_TOP_HASHES_LEMMATIZE

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
    file_list = get_atomic_file_list(path=ATOMIC_TABLES_DIR)
    for _filename in file_list:
        if _filename.endswith(".table"):
            atomic_table = load_atomic_table(_filename, path=ATOMIC_TABLES_DIR)
            _id = _filename.split(".")[0]
            atomic_table_ids.append(_id)
            atomic_tables.append(atomic_table)
    return (atomic_table_ids, atomic_tables)

def load_atomic_tables_lazy():
    file_list = get_atomic_file_list(path=ATOMIC_TABLES_DIR)
    for _filename in file_list:
        if _filename.endswith(".table"):
            atomic_table = load_atomic_table(_filename, path=ATOMIC_TABLES_DIR)
            _id = _filename.split(".")[0]
            yield (_id, atomic_table)

def get_atomic_table(_id, path=ATOMIC_TABLES_DIR):
    filename = os.path.join(path, "%s.table" % _id)
    table = load_atomic_table(filename)
    return table

def get_atomic_table_parent_id(_id):
    cmd = "grep %s %s" % (_id, ATOMIC_TABLES_INDEX,)
    stdoutdata = subprocess.getoutput(cmd)
    return stdoutdata.split(",")[0]

def get_atomic_file_list(path=ATOMIC_TABLES_DIR):
    return os.listdir(ATOMIC_TABLES_DIR)

def load_atomic_table(_filename, path=ATOMIC_TABLES_DIR):
    filepath = os.path.join(path, _filename)
    _f = open(filepath, "rb")
    atomic_table = msgpack.unpackb(_f.read())
    _f.close()
    return atomic_table

def load_random_atomic_table():
    file_list = get_atomic_file_list(path=ATOMIC_TABLES_DIR)
    _filename = random.choice(file_list)
    _id = _filename.split(".")[0]
    atomic_table = load_atomic_table(_filename, path=ATOMIC_TABLES_DIR)
    return (_id, atomic_table)

def get_table_groups(vectorization_type="simple"):
    if vectorization_type == "simple":
        _cache = ATOMIC_TABLES_TOP_HASHES_SIMPLE
    elif vectorization_type == "lemmatize":
        _cache = ATOMIC_TABLES_TOP_HASHES_LEMMATIZE

    _f = open(_cache, "rb")
    table_groups = pickle.load(_f)
    _f.close()
    return table_groups

def get_table_group_by_hash(_hash, vectorization_type="simple"):
    table_groups = get_table_groups(vectorization_type=vectorization_type)
    return get_tables_by_hash(_hash, table_groups)

def get_tables_by_hash(_hash, table_groups):
    table_ids = table_groups[_hash]
    tables = []
    for table_id in table_ids:
        table = get_atomic_table(table_id)
        tables.append(table)
    return tables

def load_table_groups_lazy(vectorization_type="simple"):
    table_groups = get_table_groups(vectorization_type=vectorization_type)
    for _hash in table_groups:
        yield (_hash, get_tables_by_hash(_hash, table_groups))
