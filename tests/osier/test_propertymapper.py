from osier.tablefactory import get_table_group_by_hash
from osier.join import join_tables_by_subject_column
from osier.propertymapper import map_table_properties

CARDINALS_HASH = 18433
def test_map_atomic_table_property():
    tables = get_table_group_by_hash(CARDINALS_HASH, vectorization_type="lemmatize")
    joined_table = join_tables_by_subject_column(tables)
    _property = map_table_properties(joined_table)
    import ipdb; ipdb.set_trace()
