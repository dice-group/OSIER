import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "..", "data")
ATOMIC_TABLES_DIR = os.path.join(DATA_DIR, "atomic_tables")
ATOMIC_TABLES_INDEX = os.path.join(DATA_DIR, "atomic_tables.index")
ATOMIC_TABLES_TOP_HASHES = os.path.join(DATA_DIR, "candidates_top_hash.data")
