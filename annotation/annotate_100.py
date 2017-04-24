import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TABLES_DIR = os.path.join(CURRENT_DIR, "tables")
SUBJECT_COLUMN_FILE = os.path.join(CURRENT_DIR, "subject_columns.csv")

from osier.tablefactory import get_table_list, get_one_table, get_random_table

def annotate():
    tables = []
    for i in range(0, 100):
        table = get_random_table()
        table_filename = table._id + ".csv"
        table_filepath = os.path.join(TABLES_DIR, table_filename)

        _f = open(table_filepath, "w")
        _f.write(table.raw_table)
        _f.close()

        print(table.raw_table)
        subject_column = input("Subject column: ")
        _f = open(SUBJECT_COLUMN_FILE, "a+")
        line = "%s,%s\n" % (table_filename, subject_column)
        _f.write(line)
        print("\n")

if __name__ == "__main__":
    annotate()
