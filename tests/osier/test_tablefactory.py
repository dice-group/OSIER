"""Test for osier/tablefactory.py"""

import random

from osier.tablefactory import get_table_list, get_one_table, get_random_table

LIST_FIRST_ITEM = "0010e112-d867-43d3-8ce2-1bf9494e3f82"
LIST_LAST_ITEM = "fff5d9c0-ea24-4d2e-a48d-a97e6b11ab9d"

ONE_HEADER = ['label', 'character']
ONE_DATA = [['Yuri Yamaoka', 'Person'], ['Yūki Kaneko', 'NaturalPerson'], ['KyoWusi Tsukui', 'Aagen'], ['Mioko Fujiwara', 'Thing'], ['Asuka Tanii', 'artist']]

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
