from scipy.stats import mode

from osier.lemmatize import lemmatize_table, lemmatize_column

def infer_table_class(table, rows=30, skip_header=False):
    """Simply returning a mode of a lemma vector."""
    if skip_header:
        table = table[1:]
    lemma_vector = lemmatize_table(table, rows=rows)
    if lemma_vector:
        return mode(lemma_vector).mode.item()
    else:
        return b""

def infer_column_name(column, rows=30, skip_header=False):
    if skip_header:
        column = column[1:]
    lemma_vector = lemmatize_column(column, rows=rows)
    if lemma_vector:
        return mode(lemma_vector).mode.item()
    else:
        return b""
