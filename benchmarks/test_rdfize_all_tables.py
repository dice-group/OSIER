from osier.rdfize import rdfize_table
from osier.tablefactory import get_table_group_by_hash, load_table_groups_lazy
from osier.join import join_tables, columnize_table

CARDINALS_HASH = 18433
def test_rdfize_table():
    for (_hash, table_group) in load_table_groups_lazy(vectorization_type="lemmatize"):
        print(_hash)
        joined_table = join_tables(table_group)
        #if table got more than 10 columns, skip!
        if(len(joined_table[0]) > 10):
            continue
        #skip table groups with more than 1000 tables
        if(len(table_group) > 1000):
            continue
        rdf = rdfize_table(joined_table)
        print(rdf.decode())
