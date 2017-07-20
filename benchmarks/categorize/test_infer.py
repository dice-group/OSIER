import pprint
pprinter = pprint.PrettyPrinter()


from osier.tablefactory import load_table_groups_lazy
from osier.join import join_tables, columnize_table
from osier.infer import infer_table_class, infer_column_name, infer_table_class_by_category

def test_join():
    for (_hash, table_group) in load_table_groups_lazy(vectorization_type="lemmatize"):
        print(_hash)
        joined_table = join_tables(table_group)
        #show 10 lines of joined table
        pprinter.pprint(joined_table[:10])
        print("Table class: %s" %(infer_table_class_by_category(joined_table, skip_header=True)))
        # col_table = columnize_table(joined_table)
        # for col in col_table:
        #     print("Column header: %s" % col[0])
        #     print("Column property: %s" % infer_column_name(col, skip_header=True))
        # print("")
