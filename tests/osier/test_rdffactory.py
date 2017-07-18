import random

from osier.rdffactory import get_all_triples, get_triples_for_table_id
from osier.tablefactory import get_random_table, get_table_list

random.seed(a=0)
TEST_TABLE = get_random_table()

def test_get_all_triples():
    triples = get_all_triples()
    assert triples.startswith("<http://")

def test_get_triples_for_table_id():
    table_id = get_table_list()[0]
    triples = get_triples_for_table_id(table_id)
    assert triples.startswith("<http://dbpedia.org/resource/")
