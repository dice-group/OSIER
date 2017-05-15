from osier.metadata import get_table_metadata, get_table_rdf_string

TABLE_ID = "b320a106-f5df-41ce-a57d-8852fb06edb8"

def test_get_table_metadata():
    table_metadata = get_table_metadata(TABLE_ID)
    assert table_metadata

def test_get_table_rdf_string():
    table_rdf = get_table_rdf_string(TABLE_ID)
    assert len(table_rdf) > 10
