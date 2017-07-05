from scipy.stats import mode
from collections import Counter

from osier.lemmatize import lemmatize_table, lemmatize_column
from osier.categorize import categorize_table
from osier.babelnet.api import get_most_specific_term

def infer_table_class(table, rows=30, skip_header=False):
    if skip_header:
        table = table[1:]
    lemma_vector = lemmatize_table(table, rows=rows)
    if lemma_vector:
        return infer_table_class_mst(lemma_vector)
    else:
        return b""

def infer_table_class_by_category(table, rows=30, skip_header=False):
    if skip_header:
        table = table[1:]
    cats_vector = categorize_table(table, rows=rows, skip_header=skip_header)
    if cats_vector:
        category = infer_table_class_cats(cats_vector)
        if(category):
            return category[0].encode("utf-8")
        else:
            return b""
    else:
        return b""

def infer_table_class_cats(cats_vector):
    cats_vector = map(lambda x: x.lower(), cats_vector)
    counted_cats = Counter(cats_vector)
    #Return only top category
    top_n_cats = counted_cats.most_common()[0:10]
    if(len(top_n_cats) > 0):
        return top_n_cats[0]
    else:
        return None

def infer_table_class_mst(lemma_vector):
    lemma_vector = map(lambda x: x.lower(), lemma_vector)
    counted_lemmas = Counter(lemma_vector)
    top_three = get_top_n_terms(counted_lemmas, 3)
    most_specific_term = get_most_specific_term(top_three)
    return most_specific_term

def infer_table_class_mode(lemma_vector):
    return mode(lemma_vector).mode.item()

#TODO: check if this one works at all with Bytes
def get_top_n_terms(counter, top_n=3):
    n_terms = counter.most_common()[0:top_n]
    #n_terms = map(lambda x: x[0].decode("utf-8"), n_terms)
    return list(n_terms)

def infer_column_name(column, rows=30, skip_header=False):
    if skip_header:
        column = column[1:]
    lemma_vector = lemmatize_column(column, rows=rows)
    if lemma_vector:
        return mode(lemma_vector).mode.item()
    else:
        return b""
