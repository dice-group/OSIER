from osier.babelnet.api import get_lemmas_simple

def lemmatize_column(column, rows=None, skip_header=False):
    vector = []
    if skip_header:
        column = column[1:]
    if rows:
        column = column[:rows]
    for item in column:
        if item:
            vector += get_lemmas_simple(item)
    return vector

def lemmatize_atomic_table(atomic_table, skip_header=False):
    vector = lemmatize_column(atomic_table[0], skip_header=skip_header) +\
             lemmatize_column(atomic_table[1], skip_header=skip_header)
    return vector


def lemmatize_table(table, rows=None, skip_header=False):
    vector = []
    if skip_header:
        table = table[1:]
    if rows:
        table = table[:rows]
    for row in table:
        if row:
            for item in row:
                if item:
                    vector += get_lemmas_simple(item)
    return vector
