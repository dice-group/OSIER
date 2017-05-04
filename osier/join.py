from datasketch.minhash import MinHash
from osier.babelnet import get_lemmas_simple

def vectorize_atomic_table(atomic_table):
    vector = atomic_table[0] + atomic_table[1]
    return vector

def lemmatize_column(column):
    vector = []
    for item in column:
        vector += get_lemmas_simple(item)
    return vector

def lemmatize_atomic_table(atomic_table):
    vector = lemmatize_column(atomic_table[0]) +\
             lemmatize_column(atomic_table[1])
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

def join_tables(table_a, table_b):
    pass
