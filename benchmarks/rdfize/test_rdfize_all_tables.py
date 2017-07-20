import os

from osier.rdfize import rdfize_table
from osier.tablefactory import get_table_group_by_hash, load_table_groups_lazy, \
    get_hash_count
from osier.join import join_tables, columnize_table

HASH_INDEX_FILE = "hash_index"
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

CARDINALS_HASH = 18433
def test_rdfize_table():
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
        _f = open("table/{}".format(str(_hash)), "wb")
        _f.write(str(joined_table).encode("utf-8"))
        _f.close()
        rdf = rdfize_table(joined_table)
        _f = open("run/{}".format(str(_hash)), "wb")
        _f.write(rdf)
        _f.close()
        add_hash_to_processed(_hash)
        current_count += 1
