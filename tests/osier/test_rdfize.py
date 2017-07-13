from taipan.agdistis import AgdistisWrapper
from taipan.rdf.generator import generate_rdf
from taipan.osiertable import OsierTable

from osier.tablefactory import get_table_group_by_hash
from osier.join import join_tables, columnize_table
from osier.infer import infer_table_class_by_category, infer_table_properties
from osier.util import table_bytes_to_utf

CARDINALS_HASH = 18433
def test_rdfize_table():
    tables = get_table_group_by_hash(CARDINALS_HASH, vectorization_type="lemmatize")
    joined_table = join_tables(tables)
    category = infer_table_class_by_category(joined_table, skip_header=True)

    properties = infer_table_properties(joined_table)

    #entities = AGDISTIS_WRAPPER.disambiguate_table(table)
    osier_table = OsierTable(table_bytes_to_utf(joined_table))
    rdf = generate_rdf(osier_table, subject_column=[0])
    import ipdb; ipdb.set_trace()
