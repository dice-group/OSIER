from osier.tablefactory import get_table_list, get_one_table, get_random_table

def test_subject_column():
    tables = []
    for i in range(0, 100):
        table = get_random_table()
        print(table.data)
        print(table.subject_column)
        print("\n")
