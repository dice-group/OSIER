from nose.tools import nottest

from osier.tablefactory import get_table_list, get_one_table, get_random_table

@nottest
def test_subject_column():
    """
        Got 87 out of 100 right (87% precision)
    """
    tables = []
    for i in range(0, 100):
        table = get_random_table()
        print(table._id)
        print(table.raw_table)
        if table.subject_column:
            print("Subject column: %s" % table.subject_column[0])
            print("Subject columns identified: %s" % len(table.subject_column))
        print("\n")
