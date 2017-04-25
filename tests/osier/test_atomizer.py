import os

from osier.table import Table
from osier.atomizer import atomize, dump_atomic_table, \
    generate_atomic_table_id, get_atomic_table_path, update_table_index
from osier.pathes import ATOMIC_TABLES_DIR, ATOMIC_TABLES_INDEX

TEST_ID = "bf3817e4-de60-4d06-baba-95b6726a1e30"

ATOMIC_TABLES = [
    [
        ['label', 'Bill Grant (curler)', 'George Allen (ice hockey)', 'Bernie Federko', 'Brian Boitano', 'Garnet Bailey'],
        ['gossip', 'William Alexander Grant (June 16, 1882 – April 16, 1942) was a Canadian curler. He was the lead of the 1928 and 1929 Brier Champion teams (skipped by Gordon Hudson), representing Manitoba. Grant was a 1975 inductee to the Canadian Curling Hall of Fame. He died suddenly in 1942 while attending a curling meeting at the Fort Rouge Curling Club.', '', '', '', '']
    ],
    [
        ['label', 'Bill Grant (curler)', 'George Allen (ice hockey)', 'Bernie Federko', 'Brian Boitano', 'Garnet Bailey'],
        ['arsenic', 'm.01311xyw', '', '', '', '']
    ],
    [
        ['label', 'Bill Grant (curler)', 'George Allen (ice hockey)', 'Bernie Federko', 'Brian Boitano', 'Garnet Bailey'],
        ['label', 'Bill Grant (curler)', '', '', '', '']
    ],
    [
        ['label', 'Bill Grant (curler)', 'George Allen (ice hockey)', 'Bernie Federko', 'Brian Boitano', 'Garnet Bailey'],
        ['type', 'Agent', 'Person', 'jock', 'winter sport Player', 'IceHockeyPlayer']
    ]
]


def test_atomize():
    table = Table(TEST_ID)
    atomic_tables = atomize(table)
    assert len(atomic_tables[0]) == 2
    assert len(atomic_tables[0][0]) == len(atomic_tables[0][1])

def test_dump_atomic_tables():
    table = Table(TEST_ID)
    atomic_tables = atomize(table)
    atomic_table = atomic_tables[0]
    _filepath = get_atomic_table_path(atomic_table, path=ATOMIC_TABLES_DIR)
    dump_atomic_table(atomic_table, path=ATOMIC_TABLES_DIR)
    #check if file was written to the directory
    assert os.path.exists(_filepath)
    #remove the file
    os.remove(_filepath)
    assert not os.path.exists(_filepath)


TABLE_ID = "19c000d102d5b0b1dd8034ce58cf8f74"
def test_generate_atomic_table_id():
    table = Table(TEST_ID)
    atomic_tables = atomize(table)
    atomic_table = atomic_tables[0]
    _id = generate_atomic_table_id(atomic_table)
    assert _id == TABLE_ID

def test_get_atomic_table_path():
    table = Table(TEST_ID)
    atomic_tables = atomize(table)
    atomic_table = atomic_tables[0]
    _path = get_atomic_table_path(atomic_table, path=ATOMIC_TABLES_DIR)
    _PATH = os.path.join(ATOMIC_TABLES_DIR, generate_atomic_table_id(atomic_table) + ".table")
    assert _path == _PATH

def test_update_table_index():
    table_id = "table_id"
    atomic_table_id = "atomic_table_id"
    ATOMIC_TABLES_INDEX_TEST = ATOMIC_TABLES_INDEX + ".test"
    update_table_index(table_id, atomic_table_id, _index=ATOMIC_TABLES_INDEX_TEST)
    update_table_index(table_id, atomic_table_id, _index=ATOMIC_TABLES_INDEX_TEST)
    update_table_index(table_id, atomic_table_id, _index=ATOMIC_TABLES_INDEX_TEST)
    _f = open(ATOMIC_TABLES_INDEX_TEST, 'rU')
    for line in _f.readlines():
        if line.startswith(table_id):
            break
    assert line == "%s,%s\n" %(atomic_table_id, table_id)
    os.remove(ATOMIC_TABLES_INDEX_TEST)
