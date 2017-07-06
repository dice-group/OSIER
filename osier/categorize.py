from osier.babelnet.api import get_synset_category, get_synset_category_with_super

def categorize_column(column, rows=None, skip_header=False):
    vector = []
    if skip_header:
        column = column[1:]
    if rows:
        column = column[:rows]
    for item in column:
        if item:
            vector += get_synset_category(item)
    return vector


def categorize_atomic_table(atomic_table, skip_header=False):
    vector = categorize_column(atomic_table[0], skip_header=skip_header) +\
             categorize_column(atomic_table[1], skip_header=skip_header)
    return vector


def categorize_table(table, rows=None, skip_header=False):
    vector = []
    if skip_header:
        table = table[1:]
    if rows:
        table = table[:rows]
    for row in table:
        if row:
            item = row[0]
            if item:
                vector += get_synset_category(item)
    return vector
