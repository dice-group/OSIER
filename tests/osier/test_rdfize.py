from osier.rdfize import rdfize_table, get_table_class_uri
from osier.tablefactory import get_table_group_by_hash
from osier.join import join_tables, columnize_table

CARDINALS_HASH = 18433
def test_rdfize_table():
    tables = get_table_group_by_hash(CARDINALS_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    rdf = rdfize_table(joined_table)


def test_get_table_class_uri():
    tables = get_table_group_by_hash(CARDINALS_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    table_class = get_table_class_uri(joined_table)
    assert table_class == 'http://dbpedia.org/ontology/Cardinal'

def test_get_table_class_uri_empty():
    TABLE = [
        ["nothing", "special", "here"],
        ["1234", "123548", "15198"]
    ]
    table_class = get_table_class_uri(TABLE)
    assert table_class == None

TEST_HASH_1 = 123927
def test_rdfize_table_test_1():
    tables = get_table_group_by_hash(TEST_HASH_1, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    rdf = rdfize_table(joined_table)

TEST_HASH_2 = 51340
def test_rdfize_table_test_2():
    tables = get_table_group_by_hash(TEST_HASH_2, vectorization_type="lemmatize")
    assert len(tables) > 1000
