from taipan.agdistis import AgdistisWrapper
from taipan.rdf.generator import generate_rdf
from taipan.osiertable import OsierTable

from osier.infer import infer_table_class_by_category, infer_table_properties
from osier.util import table_bytes_to_utf

def rdfize_table(table):
    category = infer_table_class_by_category(table, skip_header=True)
    #properties = infer_table_properties(table)
    #entities = AGDISTIS_WRAPPER.disambiguate_table(table)
    osier_table = OsierTable(table_bytes_to_utf(table))
    print(table)
    rdf = generate_rdf(osier_table, subject_column=[0], _format="nt")
    return rdf
