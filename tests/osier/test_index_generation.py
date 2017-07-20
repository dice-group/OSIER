from os import listdir
from os.path import isfile, join

from osier.tablefactory import get_table_list
from osier.pathes import ATOMIC_TABLES_DIR, ATOMIC_TABLES_INDEX

TABLE_LIST = get_table_list()
ATOMIC_TABLES_LIST = [f for f in listdir(ATOMIC_TABLES_DIR) if isfile(join(ATOMIC_TABLES_DIR, f))]

def test_index_generation():
    _f = open(ATOMIC_TABLES_INDEX, 'rU')
    for line in _f.readlines():
        (original_table_id, atomic_table_id) = line.split(",")
        assert original_table_id in TABLE_LIST
        assert "{}.table".format(atomic_table_id.strip()) in ATOMIC_TABLES_LIST
