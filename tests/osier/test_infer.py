from osier.tablefactory import get_table_group_by_hash
from osier.infer import infer_table_class, infer_column_name
from osier.join import join_tables, columnize_table
from osier.lemmatize import lemmatize_table, lemmatize_column

EXAMPLE_HASH = 126944
def test_infer_table_class():
    tables = get_table_group_by_hash(EXAMPLE_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    _class = infer_table_class(joined_table, rows=5)
    assert _class == b"location"
    _class = infer_table_class(joined_table, rows=30)
    assert _class == b"place"

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
    from collections import Counter
    lemmas = map(lambda x: x.lower(), lemmas)
    counted_lemmas = Counter(lemmas)

    col_table = columnize_table(joined_table)
    lemmatize_column(col_table[1], skip_header=True)
    import ipdb; ipdb.set_trace()
