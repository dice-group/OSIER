from osier.tablefactory import get_table_group_by_hash
from osier.infer import infer_table_class, infer_column_name
from osier.join import join_tables, columnize_table

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
