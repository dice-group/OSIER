from nose.tools import nottest

import pickle
import os

from osier.pathes import ATOMIC_TABLES_TOP_HASHES_SIMPLE, \
    ATOMIC_TABLES_TOP_HASHES_LEMMATIZE, ATOMIC_TABLES_TOP_HASHES_CATEGORIZE
from osier.tablefactory import get_atomic_table_parent_id, get_table_list
from osier.metadata import get_table_class
from osier.table import Table

def test_find_join_candidates_categorize():
    """
    Total groups: 3401
    groups with more than 1 table: 1516
    groups with more than 1 class: 832
    correct groups: 684
    """
    _f = open(ATOMIC_TABLES_TOP_HASHES_CATEGORIZE, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    print_stats(join_candidates)
    print(count_tables(join_candidates))
    print(get_groups_with_one_class(join_candidates))

@nottest
def test_find_join_candidates_lemmatize():
    """
    Total groups: 388
    groups with more than 1 table: 221
    groups with more than 1 class: 149
    correct groups: 72
    correct_hashes = [18433, 71699, 13341, 162849, 95271, 79913, 19503, 34867, 75828, 218174, 29787, 41073, 100371, 1811, 78979, 5275, 92325, 58536, 64717, 55520, 13546, 152811, 57594, 53521, 78131, 156984, 1247, 63370, 27189, 60763, 152932, 2965, 115606, 29161, 29407, 97753, 49628, 51687, 19973, 523, 24113, 127550, 117341, 68197, 78953, 124601, 150203, 60094, 27677, 83661, 119589, 50928, 113427, 118563, 112781, 31583, 125800, 115563, 409277, 6016, 56837, 137109, 55192, 3509, 162739, 94134, 80572, 55270, 79856, 80553, 25594, 43005]
    This approach join tables into groups which belongs to classes
    """
    _f = open(ATOMIC_TABLES_TOP_HASHES_LEMMATIZE, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    print_stats(join_candidates)
    print(count_tables(join_candidates))
    print(get_groups_with_one_class(join_candidates))

@nottest
def test_find_join_candidates():
    """
    Total tables: 8619
    total groups: 5962
    groups with one table: 4540
    groups with more than one table: 1422
    groups with more than one class (incorrect): 598
    groups with one class (correct): 824
    This can only find candidate tables which have the same values in the cells, mostly joining the tables back.
    """
    _f = open(ATOMIC_TABLES_TOP_HASHES_SIMPLE, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    print_stats(join_candidates)
    print(count_tables(join_candidates))

def count_tables(join_candidates):
    count = 0
    for _hash in join_candidates:
        count += len(join_candidates[_hash])
    return count

def print_stats(join_candidates):
    (number_of_groups, no_groups_more_than_one_class) = count_groups(
        join_candidates)
    print(len(join_candidates))
    print(number_of_groups)
    print(no_groups_more_than_one_class)

def count_groups(join_candidates):
    number_of_groups = 0
    no_groups_more_than_one_class = 0
    for num, _hash_value in enumerate(join_candidates):
        print("%s out of %s" % (num, len(join_candidates),))
        if len(join_candidates[_hash_value]) <= 1:
            continue
        number_of_groups += 1
        prev_class = None
        for atomic_table_id in join_candidates[_hash_value]:
            parent_id = get_atomic_table_parent_id(atomic_table_id)
            _class = get_table_class(parent_id)
            if prev_class:
                if _class != prev_class:
                    no_groups_more_than_one_class += 1
                    break
            prev_class = _class
    return (number_of_groups, no_groups_more_than_one_class)

def get_groups_with_more_than_one_class(join_candidates):
    _hashes = []
    for num, _hash_value in enumerate(join_candidates):
        if len(join_candidates[_hash_value]) <= 1:
            continue
        prev_class = None
        for atomic_table_id in join_candidates[_hash_value]:
            parent_id = get_atomic_table_parent_id(atomic_table_id)
            _class = get_table_class(parent_id)
            if prev_class:
                if _class != prev_class:
                    _hashes.append(_hash_value)
                    break
            prev_class = _class
    return _hashes

def get_groups_with_one_class(join_candidates):
    more_than_one_class = get_groups_with_more_than_one_class(join_candidates)
    _hashes = []
    for num, _hash_value in enumerate(join_candidates):
        if len(join_candidates[_hash_value]) <= 1:
            continue
        if not _hash_value in more_than_one_class:
            _hashes.append(_hash_value)
    return _hashes

# Remove the following tables from the corpus (10%)
BLACK_LIST = [
    "ac058b55-a17d-42ef-969e-2077ba39d1cd"
]

@nottest
def test_find_join_candidates_upper_limit():
    """
        total groups: 451 (number of classes)
        with more than one item: 451
        with more than one class: 0
    """
    table_list = get_table_list()
    print(len(table_list))
    return 0
    join_candidates = {}
    for table_id in table_list:
        if table_id in BLACK_LIST:
            continue
        _class = get_table_class(table_id)
        if not _class['URI'] in join_candidates:
            join_candidates[_class['URI']] = []
        join_candidates[_class['URI']].append(table_id)
    count = 0
    for class_uri in join_candidates:
        if len(join_candidates[class_uri]) > 1:
            count += 1
    print(len(join_candidates))
    print(count)


PLACES_HASH = 126944
EDUCATIONAL_FACILITIES_HASH = 48940
CURRENCY_HASH = 97753
WARS_HASH = 53
@nottest
def test_join_tables():
    # get join candidates
    _f = open(ATOMIC_TABLES_TOP_HASHES_LEMMATIZE, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    _random_hash = random.choice(list(join_candidates.keys()))
    print(_random_hash)
    table_ids = join_candidates[_random_hash]
    tables = []
    for table_id in table_ids:
        table = get_atomic_table(table_id)
        tables.append(table)
