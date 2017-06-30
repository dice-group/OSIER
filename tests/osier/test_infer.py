from osier.tablefactory import get_table_group_by_hash
from osier.infer import infer_table_class, infer_column_name, get_top_n_terms
from osier.join import join_tables, columnize_table
from osier.lemmatize import lemmatize_table, lemmatize_column

EXAMPLE_HASH = 126944
def test_infer_table_class():
    tables = get_table_group_by_hash(EXAMPLE_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)

    _class = infer_table_class(joined_table, rows=5)
    assert _class == "label"
    _class = infer_table_class(joined_table, rows=30)
    assert _class == "place"

def test_infer_column_name():
    tables = get_table_group_by_hash(EXAMPLE_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    col_table = columnize_table(joined_table)
    column_name = infer_column_name(col_table[0])
    assert column_name == b"label"
    column_name = infer_column_name(col_table[1])
    assert column_name == b"place"

PROBLEMATIC_HASH = 123927
def test_infer():
    tables = get_table_group_by_hash(PROBLEMATIC_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    _class = infer_table_class(joined_table, rows=5)
    #print(_class)

CARDINALS_HASH = 18433
def test_infer_cardinals():
    tables = get_table_group_by_hash(CARDINALS_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    lemmas = lemmatize_table(joined_table)
    table_class = infer_table_class(joined_table, skip_header=True)
    assert table_class == "cardinal"

def test_get_top_n_terms():
    from collections import Counter
    _array = [b"a", b"a", b"a", b"b", b"c", b"d", b"d", b"d", b"d", b"d", b"d", b"f", b"f"]
    counted = Counter(_array)
    top_n = get_top_n_terms(counted)
    assert top_n == ['d', 'a', 'f']
