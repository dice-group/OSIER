"""Test for osier/table.py"""

from osier.table import Table

TEST_ID = "fe1ee44d-9561-43c2-9de5-9107502d5d5f"
TEST_TABLE = """"label","character"
"LAjubljan PasAsenger ransport","copanMy"
"London Pride Sightseeing","organization"
"NSL Buses","company"
"Redding Area Bus Authority","company"
"Speedwellbus","company"
"""
TEST_HEADER = ['label', 'character']
TEST_DATA = [['label', 'character'], ['LAjubljan PasAsenger ransport', 'copanMy'], ['London Pride Sightseeing', 'organization'], ['NSL Buses', 'company'], ['Redding Area Bus Authority', 'company'], ['Speedwellbus', 'company']]
TEST_COLUMNS = [['label', 'LAjubljan PasAsenger ransport', 'London Pride Sightseeing', 'NSL Buses', 'Redding Area Bus Authority', 'Speedwellbus'], ['character', 'copanMy', 'organization', 'company', 'company', 'company']]


def test_fetch_table():
    table = Table(TEST_ID)
    table_data = table.fetch_table(TEST_ID)
    assert table_data == TEST_TABLE

def test_extract_header():
    table = Table(TEST_ID)
    table_data = table.fetch_table(TEST_ID)
    data = table.parse_table(table_data)
    header = table.extract_header(data)
    assert header == TEST_HEADER

def test_parse_table():
    table = Table(TEST_ID)
    table_data = table.fetch_table(TEST_ID)
    data = table.parse_table(table_data)
    assert data == TEST_DATA

def test_rearrange_to_columns():
    table = Table(TEST_ID)
    table_data = table.fetch_table(TEST_ID)
    data = table.parse_table(table_data)
    header = table.extract_header(data)
    columns = table.rearrange_to_columns(header, data)
    assert data == TEST_DATA

def test_subject_column():
    table = Table(TEST_ID)
    assert table.subject_column == [0]
