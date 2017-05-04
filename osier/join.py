from datasketch.minhash import MinHash

def vectorize_atomic_table(atomic_table):
    vector = atomic_table[0] + atomic_table[1]
    return vector

def extract_senses(atomic_table):
    #need another class for the babelnet interface -- better lib
    pass

def get_hash_values(atomic_table):
    table_vector = vectorize_atomic_table(atomic_table)
    _hash = MinHash()
    for item in table_vector:
        _hash.update(item)
    return _hash.hashvalues

def get_top_hash(atomic_table):
    hash_values = get_hash_values(atomic_table)
    hash_values.sort()
    return hash_values[0]

def join_tables(table_a, table_b):
    pass
