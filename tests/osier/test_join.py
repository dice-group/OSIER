from nose.tools import nottest

import pickle
import numpy
import random

from osier.pathes import ATOMIC_TABLES_TOP_HASHES_LEMMATIZE
from osier.join import vectorize_atomic_table, get_hash_values, \
    get_top_hash, join_tables_by_subject_column, lemmatize_column, \
    lemmatize_atomic_table, get_atomic_table_header, squash_headers, \
    join_tables_by_subject_column, align_size_of_virtual_table, \
    linearize_table, deduplicate_table, join_two_rows, \
    join_tables
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


TEST_TABLES = [
    [
        [b'label', b'Lower Jurala Hydro Electric Project', b'Lianhua Dam', b'Maerdang Dam', b'San Clemente Dam', b'HoovVerDam'],
        [b'type', b'Place', b'architectural structure', b'Thing', b'Location', b'dEed']
    ],
    [
        [b'label', b'Padthaway wine region', b'Robe wine region', b'Currency Creek wine region', b'Tokaj (Slovakia)', b'Adelaide Plains wine region'],
        [b'type', b'Location', b'Location', b'Location', b'Location', b'Thing']
    ],
    [
        [b'label', b'Lower Jurala Hydro Electric Project', b'Lianhua Dam', b'Maerdang Dam', b'San Clemente Dam', b'HoovVerDam'],
        [b'location', b'New York', b'London', b'Vietnam', b'Berlin', b'Astana']
    ]
]

JOINED_TABLE = [
    [b'label', b'Lower Jurala Hydro Electric Project', b'Lianhua Dam', b'Maerdang Dam', b'San Clemente Dam', b'HoovVerDam', b'Padthaway wine region', b'Robe wine region', b'Currency Creek wine region', b'Tokaj (Slovakia)', b'Adelaide Plains wine region', b'Lower Jurala Hydro Electric Project', b'Lianhua Dam', b'Maerdang Dam', b'San Clemente Dam', b'HoovVerDam'],
    [b'type', b'Place', b'architectural structure', b'Thing', b'Location', b'dEed', b'Location', b'Location', b'Location', b'Location', b'Thing', None, None, None, None, None],
    [b'location', None, None, None, None, None, None, None, None, None, None, b'New York', b'London', b'Vietnam', b'Berlin', b'Astana']
]

def test_join_tables_by_subject_column():
    joined_table = join_tables_by_subject_column(TEST_TABLES)
    assert joined_table == JOINED_TABLE

def test_get_atomic_table_header():
    header = get_atomic_table_header(TEST_TABLES[0])
    assert header == [b'label', b'type']

def test_squash_headers():
    virtual_header = squash_headers(TEST_TABLES)
    assert virtual_header == [b'label', b'type', b'location']

VIRTUAL_TABLE = {
        b'label': [b'Lower Jurala Hydro Electric Project', b'Lianhua Dam', b'Maerdang Dam', b'San Clemente Dam', b'HoovVerDam'],
        b'type': [b'New York', b'London', b'Vietnam', b'Berlin', b'Astana'],
        b'location': []
    }

def test_align_size_of_virtual_table():
    aligned_table = align_size_of_virtual_table(VIRTUAL_TABLE)
    for _key in aligned_table:
        assert len(aligned_table[_key]) == 5

LINEAR_TABLE = [
 [b'label', b'type', b'location'],
 [b'Lower Jurala Hydro Electric Project', b'Place', None],
 [b'Lianhua Dam', b'architectural structure', None],
 [b'Maerdang Dam', b'Thing', None],
 [b'San Clemente Dam', b'Location', None],
 [b'HoovVerDam', b'dEed', None],
 [b'Padthaway wine region', b'Location', None],
 [b'Robe wine region', b'Location', None],
 [b'Currency Creek wine region', b'Location', None],
 [b'Tokaj (Slovakia)', b'Location', None],
 [b'Adelaide Plains wine region', b'Thing', None],
 [b'Lower Jurala Hydro Electric Project', None, b'New York'],
 [b'Lianhua Dam', None, b'London'],
 [b'Maerdang Dam', None, b'Vietnam'],
 [b'San Clemente Dam', None, b'Berlin'],
 [b'HoovVerDam', None, b'Astana']
]

def test_linearize_table():
    linear_table = linearize_table(JOINED_TABLE)
    assert linear_table == LINEAR_TABLE

SORTED_LINEAR_TABLE = [
    [b'Adelaide Plains wine region', b'Thing', None],
    [b'Currency Creek wine region', b'Location', None],
    [b'HoovVerDam', b'dEed', None],
    [b'HoovVerDam', None, b'Astana'],
    [b'Lianhua Dam', b'architectural structure', None],
    [b'Lianhua Dam', None, b'London'],
    [b'Lower Jurala Hydro Electric Project', b'Place', None],
    [b'Lower Jurala Hydro Electric Project', None, b'New York'],
    [b'Maerdang Dam', b'Thing', None],
    [b'Maerdang Dam', None, b'Vietnam'],
    [b'Padthaway wine region', b'Location', None],
    [b'Robe wine region', b'Location', None],
    [b'San Clemente Dam', b'Location', None],
    [b'San Clemente Dam', None, b'Berlin'],
    [b'Tokaj (Slovakia)', b'Location', None]]

def test_join_two_rows():
    joined_row = join_two_rows(SORTED_LINEAR_TABLE[2], SORTED_LINEAR_TABLE[3])
    assert joined_row == [b'HoovVerDam', b'dEed', b'Astana']

DEDUPLICATED_TABLE = [
    [b'label', b'type', b'location'],
    [b'Adelaide Plains wine region', b'Thing', None],
    [b'Currency Creek wine region', b'Location', None],
    [b'HoovVerDam', b'dEed', b'Astana'],
    [b'Lianhua Dam', b'architectural structure', b'London'],
    [b'Lower Jurala Hydro Electric Project', b'Place', b'New York'],
    [b'Maerdang Dam', b'Thing', b'Vietnam'],
    [b'Padthaway wine region', b'Location', None],
    [b'Robe wine region', b'Location', None],
    [b'San Clemente Dam', b'Location', b'Berlin'],
    [b'Tokaj (Slovakia)', b'Location', None]
]

def test_deduplicate_table():
    dedup_table = deduplicate_table(JOINED_TABLE)
    assert dedup_table == DEDUPLICATED_TABLE

def test_join_tables():
    table = join_tables(TEST_TABLES)
    assert table == DEDUPLICATED_TABLE
