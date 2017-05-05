"""Test for osier/tablefactory.py"""

from nose.tools import nottest
import random

from osier.tablefactory import get_table_list, get_one_table, \
    get_random_table, load_atomic_tables, load_random_atomic_table, \
    load_atomic_tables_lazy, get_atomic_table, get_atomic_table_parent_id, \
    get_table_group_by_hash, load_table_groups_lazy
from osier.atomizer import generate_atomic_table_id

LIST_FIRST_ITEM = "001351a2-73fd-4550-be6c-601c98392acb"
LIST_LAST_ITEM = "fff5d9c0-ea24-4d2e-a48d-a97e6b11ab9d"

ONE_HEADER = ['label', 'character']
ONE_DATA = [['label', 'character'], ['Dinagat bushy-tailed cloud rat', 'brute'], ['Dinagat gymnure', 'object'], ['Eastern red bat', 'object'], ['Fairway (horse)', 'equine'], ['Flares (horse)', 'horse']]

ATOMIC_TABLE_ID = "35bf0edce0184a9b14e9a3f65047e94c"

def test_get_table_list():
    table_list = get_table_list()
    assert table_list[0] == LIST_FIRST_ITEM
    assert table_list[-1] == LIST_LAST_ITEM

def test_get_one_table():
    table = get_one_table(100)
    assert table.data == ONE_DATA
    assert table.header == ONE_HEADER

    the_same_table = get_one_table(100 + len(get_table_list()))
    assert table.data == ONE_DATA
    assert table.header == ONE_HEADER

def test_get_random_table():
    """This test is deterministic because we set seed value."""
    random.seed(a=0)
    table_a = get_random_table()
    table_b = get_random_table()
    assert table_a.data != table_b.data

@nottest
def test_load_atomic_tables():
    """Takes to long to load"""
    (atomic_table_ids, atomic_tables) = load_atomic_tables()
    _ID = generate_atomic_table_id(atomic_tables[0])
    assert atomic_table_ids[0] == _ID
    assert len(atomic_tables[0][0]) == len(atomic_tables[0][1])
    assert len(atomic_tables[0]) == 2

def test_load_random_atomic_table():
    """Tables without subject column were split into single columns"""
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    _ID = generate_atomic_table_id(atomic_table)
    assert atomic_table_id == _ID
    assert len(atomic_table[0]) == len(atomic_table[1])
    assert len(atomic_table) == 2

def test_load_atomic_tables_lazy():
    for _id, atomic_table in load_atomic_tables_lazy():
        _ID = generate_atomic_table_id(atomic_table)
        assert _ID == _id
        break

def test_get_atomic_table():
    atomic_table = get_atomic_table(ATOMIC_TABLE_ID)
    assert len(atomic_table[0]) == len(atomic_table[1])
    assert len(atomic_table) == 2

def test_get_atomic_table_parent_id():
    table_parent = get_atomic_table_parent_id(ATOMIC_TABLE_ID)
    assert table_parent == "b320a106-f5df-41ce-a57d-8852fb06edb8"


PLACES_HASH = 126944
def test_get_table_group_by_hash():
    tables = get_table_group_by_hash(PLACES_HASH, vectorization_type="lemmatize")
    assert len(tables) > 3


def test_load_table_groups_lazy():
    for table_group in load_table_groups_lazy(vectorization_type="lemmatize"):
        assert len(table_group) > 2
        break
