from statistics import mode

from osier.join import lemmatize_table, lemmatize_column

def infer_table_class(table, rows=30):
    """Simply returning a mode of a lemma vector."""
    lemma_vector = lemmatize_table(table, rows=rows)
    return mode(lemma_vector)

def infer_column_name(column, rows=None):
    lemma_vector = lemmatize_column(column, rows=rows)
    return mode(lemma_vector)
