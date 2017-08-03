import os
from collections import Counter
from nose.tools import nottest

from osier.rdfize import rdfize_table
from osier.tablefactory import get_table_group_by_hash, load_table_groups_lazy, \
    get_hash_count
from osier.join import join_tables, columnize_table
from osier.propertymapper import map_table_properties

HASH_INDEX_FILE = "hash_index_property_mapping"
def is_hash_to_processed(_hash):
    _hash = str(_hash)
    if not os.path.exists(HASH_INDEX_FILE):
        return False
    _f = open(HASH_INDEX_FILE, "r+")
    for line in _f.readlines():
        if _hash == line.strip():
            _f.close()
            return True
    _f.close()
    return False

def add_hash_to_processed(_hash):
    _hash = str(_hash)
    _f = open(HASH_INDEX_FILE, "a+")
    _f.write(_hash+"\n")
    _f.close()

def test_calculate_properties():
    hash_count = get_hash_count(vectorization_type="lemmatize")
    current_count = 0
    for (_hash, table_group) in load_table_groups_lazy(vectorization_type="lemmatize"):
        print("Processing {} out of {}".format(current_count, hash_count))
        if is_hash_to_processed(_hash):
            current_count += 1
            continue
        joined_table = join_tables(table_group)
        #if table got more than 10 columns, skip!
        if(len(joined_table[0]) > 10):
            continue
        #skip table groups with more than 1000 tables
        if(len(table_group) > 1000):
            continue
        #if table got more than 10 columns, skip!
        _f = open("table/{}".format(str(_hash)), "wb")
        _f.write(str(joined_table).encode("utf-8"))
        _f.close()
        _properties = map_table_properties(joined_table, rows_to_analyze=5)
        _f = open("run/{}".format(str(_hash)), "wb")
        _f.write(str(_properties).encode())
        _f.close()
        add_hash_to_processed(_hash)
        current_count += 1

import pprint
pprinter = pprint.PrettyPrinter()

@nottest
def test_get_top_properties():
    with open("hash_index_property_mapping") as f:
        for _hash in f.readlines():
            _hash = _hash.strip()
            with open("table/{}".format(_hash)) as table:
                _table = eval(table.readlines()[0])
            with open("run/{}".format(_hash)) as properties:
                _properties = eval(properties.readlines()[0])
            for column_pair in _properties:
                counter = Counter(_properties[column_pair])
                print(_hash)
                print(column_pair)
                print(counter)
                pprinter.pprint(_table[0:5])
                print()
