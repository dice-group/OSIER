from taipan.agdistis import AgdistisWrapper
from taipan.rdf.generator import generate_rdf
from taipan.osiertable import OsierTable
from taipan.recommender.classes.lov import get_table_class

from osier.infer import infer_table_class, infer_table_properties
from osier.util import table_bytes_to_utf

def rdfize_table(table):
    osier_table = OsierTable(table_bytes_to_utf(table))
    #Generate RDF based on properties
    table_class_uri = get_table_class_uri(table)
    rdf = generate_rdf(osier_table, subject_column=[0], _format="nt", table_class=table_class_uri, skip_header=True)
    #Generate types
    return rdf

def get_table_class_uri(table):
    category = infer_table_class(table, skip_header=True)
    table_class = get_table_class(category)
    if table_class:
        return table_class[0]["uri"]
    else:
        return None
