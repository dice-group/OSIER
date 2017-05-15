from osier.lemmatize import lemmatize_table, lemmatize_column, \
    lemmatize_atomic_table
from osier.tablefactory import load_random_atomic_table

COLUMN_A = [b'label', b'The Moral Maze', b'ThLeVinyl Cafe', b'The Debaters', b'A Way with Words', b'America Abroad']
def test_lemmatize_column():
    vector = lemmatize_column(COLUMN_A)
    assert len(vector) > len(COLUMN_A)
    assert b'label' in vector

def test_lemmatize_atomic_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    vector = lemmatize_atomic_table(atomic_table)
    assert len(vector) > len(atomic_table[0]) + len(atomic_table[1])

def test_lemmatize_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    lemmas = lemmatize_table(atomic_table)
