import msgpack
import os

from osier.pathes import ATOMIC_TABLES_DIR
from osier.util import generate_id

def atomize(table):
    if table.subject_column:
        subject_column = table.subject_column[0]
    else:
        return table.columns

    atomic_tables = []

    for i in range(0, len(table.columns)):
        if i == subject_column:
            continue
        atomic_table = []
        atomic_table.append(table.columns[subject_column])
        atomic_table.append(table.columns[i])
        atomic_tables.append(atomic_table)
    return atomic_tables

def dump_atomic_table(table, path=ATOMIC_TABLES_DIR):
    table_byte_string = msgpack.packb(table)
    table_id = generate_atomic_table_id(table)
    filepath = get_atomic_table_path(table, path=ATOMIC_TABLES_DIR)
    if not os.path.exists(filepath):
        _f = open(filepath, "wb")
        _f.write(table_byte_string)
        _f.close()

def generate_atomic_table_id(table):
    table_byte_string = msgpack.packb(table)
    return generate_id(table_byte_string)

def get_atomic_table_path(table, path=ATOMIC_TABLES_DIR):
    table_id = generate_atomic_table_id(table)
    return os.path.join(path, table_id + ".table")
