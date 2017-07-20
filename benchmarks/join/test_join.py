import pprint
pprinter = pprint.PrettyPrinter()


from osier.tablefactory import load_table_groups_lazy
from osier.join import join_tables

def test_join():
    for (_hash, table_group) in load_table_groups_lazy(vectorization_type="lemmatize"):
        print(_hash)
        join_tables(table_group)
        pprinter.pprint(join_tables(table_group))
