import pickle
import numpy

from osier.pathes import ATOMIC_TABLES_TOP_HASHES
from osier.join import vectorize_atomic_table, get_hash_values, \
    get_top_hash, join_tables
from osier.tablefactory import load_random_atomic_table, get_atomic_table

def test_vectorize_atomic_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    vector = vectorize_atomic_table(atomic_table)
    assert isinstance(vector, list)
    assert isinstance(vector[0], bytes)
    assert len(vector) > 0

def test_get_hash_values():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    hash_values = get_hash_values(atomic_table)
    assert len(hash_values) == 128
    assert isinstance(hash_values[0], numpy.uint64)

def test_get_top_hash():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    _hash = get_top_hash(atomic_table)
    assert isinstance(_hash, numpy.uint64)


TOP_HASH = 5227332
def test_join_tables():
    # get join candidates
    _f = open(ATOMIC_TABLES_TOP_HASHES, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    table_ids = join_candidates[TOP_HASH]
    tables = []
    for table_id in table_ids:
        table = get_atomic_table(table_id)
        tables.append(table)
    import ipdb; ipdb.set_trace()
