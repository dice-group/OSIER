from taipan.mapper.properties.connectivity import map_table_properties_connectivity

from taipan.osiertable import OsierTable
from osier.util import table_bytes_to_utf

def map_table_properties(table, rows_to_analyze=10):
    osier_table = OsierTable(table_bytes_to_utf(table))
    return map_table_properties_connectivity(osier_table, rows_to_analyze=rows_to_analyze)
