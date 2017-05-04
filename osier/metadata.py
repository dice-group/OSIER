"""Table wrapper class"""

import requests
import os
import json

OSIER_DATA_ENDPOINT = os.environ.get("OSIER_DATA_ENDPOINT", "http://localhost")
METADATA_URI = OSIER_DATA_ENDPOINT + "/metadata/"
RDF_URI = OSIER_DATA_ENDPOINT + "/triples/"

def get_table_metadata(_id):
    r = requests.get(METADATA_URI + _id)
    r.raise_for_status()
    metadata_string = r.content.decode("utf-8")
    return json.loads(metadata_string)

def get_table_class(_id):
    return get_table_metadata(_id)["class"]

def get_table_properties(_id):
    return get_table_metadata(_id)["properties"]

def get_table_subject_column(_id):
    return get_table_metadata(_id)["subject_column"]

def get_table_rdf_string(_id):
    r = requests.get(RDF_URI + _id + ".nt")
    r.raise_for_status()
    return r.content.decode("utf-8")
