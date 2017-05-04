import pickle
import numpy

from osier.pathes import ATOMIC_TABLES_TOP_HASHES
from osier.join import vectorize_atomic_table, get_hash_values, \
    get_top_hash, join_tables, lemmatize_column, lemmatize_atomic_table
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
    hash_values_simple = get_hash_values(atomic_table, vectorization_type="simple")
    hash_values_lemmatize = get_hash_values(atomic_table, vectorization_type="lemmatize")
    assert len(hash_values_simple) == 128
    assert len(hash_values_lemmatize) == 128
    assert isinstance(hash_values_simple[0], numpy.uint64)
    assert isinstance(hash_values_lemmatize[0], numpy.uint64)

def test_get_top_hash():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    _hash_simple = get_top_hash(atomic_table, vectorization_type="simple")
    _hash_lemmatize = get_top_hash(atomic_table, vectorization_type="lemmatize")
    assert isinstance(_hash_simple, numpy.uint64)
    assert isinstance(_hash_lemmatize, numpy.uint64)


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

COLUMN_A = [b'label', b'The Moral Maze', b'ThLeVinyl Cafe', b'The Debaters', b'A Way with Words', b'America Abroad']
def test_lemmatize_column():
    vector = lemmatize_column(COLUMN_A)
    assert len(vector) > len(COLUMN_A)
    assert b'label' in vector

def test_lemmatize_atomic_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    vector = lemmatize_atomic_table(atomic_table)
    assert len(vector) > len(atomic_table[0]) + len(atomic_table[1])
