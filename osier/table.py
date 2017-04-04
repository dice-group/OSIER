"""Table wrapper class"""

import requests
import os

OSIER_DATA_ENDPOINT = os.environ.get("OSIER_DATA_ENDPOINT", "http://localhost")
TABLE_URI = OSIER_DATA_ENDPOINT + "/table/csv/"

class Table(object):
    def __init__(self, _id):
        self._id = _id
        self.table = self.fetch_table(_id)
        self.header = self.extract_header(self.table)
        self.data = self.extract_data(self.table)
        self.columns = self.rearrange_to_columns(self.header, self.data)

    def fetch_table(self, _id):
        r = requests.get(TABLE_URI + _id + ".csv")
        r.raise_for_status()
        return r.content.decode("utf-8")

    def extract_header(self, table):
        header = []
        header_string = table.split("\n")[0]
        for item in header_string.split('","'):
            header.append(item.replace('"', ''))
        return header

    def extract_data(self, table):
        data = []
        table_lines = table.split("\n")
        for i in range(1, len(table_lines)):
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
        for row in data:
            for num, item in enumerate(row):
                columns[num].append(item)
        return columns
