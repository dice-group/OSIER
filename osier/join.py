import copy

from datasketch.minhash import MinHash
from osier.lemmatize import lemmatize_atomic_table

def vectorize_atomic_table(atomic_table):
    vector = atomic_table[0] + atomic_table[1]
    return vector


def get_hash_values(atomic_table, vectorization_type="simple"):
    table_vector = []
    if vectorization_type == "simple":
        table_vector = vectorize_atomic_table(atomic_table)
    elif vectorization_type == "lemmatize":
        table_vector = lemmatize_atomic_table(atomic_table)
    _hash = MinHash()
    for item in table_vector:
        _hash.update(item)
    return _hash.hashvalues


def get_top_hash(atomic_table, vectorization_type="simple"):
    hash_values = get_hash_values(atomic_table, vectorization_type=vectorization_type)
    hash_values.sort()
    return hash_values[0]


def join_tables(atomic_tables):
    joined_table = join_tables_by_subject_column(atomic_tables)
    return deduplicate_table(joined_table)


def join_tables_by_subject_column(atomic_tables):
    #collect all headers in a virtual table
    virtual_header = squash_headers(atomic_tables)
    virtual_table = {}
    for item in virtual_header:
        virtual_table[item] = []
    #rearrange values from atomic tables into a virtual table
    for atomic_table in atomic_tables:
        for col in atomic_table:
            col_header = col[0]
            col_data = col[1:]
            virtual_table[col_header] += col_data
        virtual_table = align_size_of_virtual_table(virtual_table)
    joined_table = []
    for header_item in virtual_header:
        joined_column = [header_item]
        joined_column += virtual_table[header_item]
        joined_table.append(joined_column)
    return joined_table


def deduplicate_table(joined_table):
    deduplicated_table = []

    linear_table = linearize_table(joined_table)
    table_header = linear_table[0]
    deduplicated_table.append(table_header)

    # TODO: generate label if missing
    table_data = []
    for row in linear_table[1:]:
        if row and row[0]:
            table_data.append(row)
    table_data = sorted(table_data, key=lambda x: x[0])
    prev_row = table_data.pop(0)
    while len(table_data) > 0:
        row = table_data.pop(0)
        if prev_row:
            if row[0] == prev_row[0]:
                deduplicated_table.append(join_two_rows(prev_row, row))
                prev_row = None
                continue
            else:
                deduplicated_table.append(prev_row)
        prev_row = row
    if prev_row:
        deduplicated_table.append(prev_row)
    return deduplicated_table


def join_two_rows(row_a, row_b):
    joined_row = []
    for num, item in enumerate(row_a):
        if item:
            joined_row.append(item)
        elif row_b[num]:
            joined_row.append(row_b[num])
        else:
            joined_row.append(None)
    return joined_row


def linearize_table(table):
    rows = []
    for i in range(0, len(table[0])):
        row = []
        for col in table:
            if col:
                row.append(col[i])
        rows.append(row)
    return rows

def columnize_table(table):
    cols = []
    for i in range(0, len(table[0])):
        col = []
        for row in table:
            if row:
                col.append(row[i])
        cols.append(col)
    return cols

def align_size_of_virtual_table(virtual_table):
    virtual_header = []
    for _header_item in virtual_table.keys():
        _header_tuple = (_header_item, len(virtual_table[_header_item]))
        virtual_header.append(_header_tuple)
    virtual_header = sorted(virtual_header, key=lambda x: x[1], reverse=True)
    prev_length = None
    for (_key, length) in virtual_header:
        current_length = len(virtual_table[_key])
        if prev_length:
            if current_length < prev_length:
                virtual_table[_key] += [None]*(prev_length - current_length)
        prev_length = len(virtual_table[_key])
    return virtual_table


def squash_headers(atomic_tables):
    virtual_header = []
    for atomic_table in atomic_tables:
        for item in get_atomic_table_header(atomic_table):
            if not item in virtual_header:
                virtual_header.append(item)
    return virtual_header


def get_atomic_table_header(atomic_table):
    return [atomic_table[0][0], atomic_table[1][0]]
