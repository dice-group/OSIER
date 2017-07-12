from osier.categorize import categorize_table, categorize_column, \
    categorize_atomic_table
from osier.tablefactory import load_random_atomic_table

PORN_ACTORS_LABEL_COLUMN = [b'label', b'C\xc3\xa9line Bara', b'Eric Masterson (actor)', b'Frederick William Matthiessen', b'Gianna Michaels', b'James Deen']
def test_categorize_column():
    vector = categorize_column(PORN_ACTORS_LABEL_COLUMN, skip_header=True)
    assert len(vector) > len(PORN_ACTORS_LABEL_COLUMN)
    assert 'Living_people' in vector

def test_categorize_atomic_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    vector = categorize_atomic_table(atomic_table)
    assert len(vector) > 0

def test_categorize_table():
    while True:
        (atomic_table_id, atomic_table) = load_random_atomic_table()
        if isinstance(atomic_table[0], list):
            break
    categories = categorize_table(atomic_table)
    assert len(categories) > 0
