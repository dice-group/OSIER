"""Table wrapper class"""

import requests
import os
import numpy as np

from taipan.ml.subjectcolumn.scidentifier import SCIdentifier

SCIDENTIFIER = SCIdentifier()
OSIER_DATA_ENDPOINT = os.environ.get("OSIER_DATA_ENDPOINT", "http://localhost")
TABLE_URI = OSIER_DATA_ENDPOINT + "/table/csv/"

class Table(object):
    def __init__(self, _id):
        self._id = _id
        self.raw_table = self.fetch_table(_id)
        self.data = self.parse_table(self.raw_table)
        self.header = self.extract_header(self.data)
        self.columns = self.rearrange_to_columns(self.header, self.data)

        self.subject_column = None
        self.table = np.array(self.data)
        self.subject_column = SCIDENTIFIER.identify_subject_column(self)

    def fetch_table(self, _id):
        r = requests.get(TABLE_URI + _id + ".csv")
        r.raise_for_status()
        return r.content.decode("utf-8")

    def extract_header(self, table):
        return table[0]

    def parse_table(self, table):
        data = []
        table_lines = table.split("\n")
        for i in range(0, len(table_lines)):
            items = table_lines[i].split('","')
            if items == ['']:
                continue
            row = []
            for item in items:
                row.append(item.replace('"', ''))
            data.append(row)
        return data

    def rearrange_to_columns(self, header, data):
        columns = []
        for item in header:
            columns.append([item])
        for row in data[1:]:
            for num, item in enumerate(row):
                columns[num].append(item)
        return columns

    def is_subject_column(self, i):
        if i == self.subject_column:
            return True
        return False
