from nose.tools import nottest

import pickle
import os

from osier.pathes import ATOMIC_TABLES_TOP_HASHES
from osier.tablefactory import get_atomic_table_parent_id, get_table_list
from osier.metadata import get_table_class
from osier.table import Table

@nottest
def test_find_join_candidates():
    """
    Total tables: 8619
    total groups: 5962
    groups with one table: 4540
    groups with more than one table: 1422
    groups with more than one class (incorrect): 598
    groups with one class (correct): 824
    """
    _f = open(ATOMIC_TABLES_TOP_HASHES, "rb")
    join_candidates = pickle.load(_f)
    _f.close()
    number_of_groups = 0
    number_of_not_same_class_groups = 0
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
                    number_of_not_same_class_groups += 1
                    break
            prev_class = _class
    print(len(join_candidates))
    print(number_of_groups)
    print(number_of_not_same_class_groups)

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
