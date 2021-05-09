from typing import Optional
from .abc import AbstractTransformer
from .table import Table
import csv
import json


class Import(AbstractTransformer):
    """Importe une table csv"""
    def __init__(self, filename: str):
        self.filename = filename


class ImportCSV(Import):
    def __init__(self,
                 filename: str,
                 encoding: Optional[str] = None,
                 delimiter: Optional[str] = None):
        super().__init__(filename)
        self.delimiter = delimiter or ';'
        self.encoding = encoding or 'ISO-8859-1'

    def process(self) -> Table:
        data = []
        with open(self.filename, encoding=self.encoding) as csvfile:
            covidreader = csv.reader(csvfile, delimiter=self.delimiter)
            for row in covidreader:
                data.append(row)
        result = Table(data.pop(0))
        for item in data:
            result.append_row(item)
        return result

    def transform(self) -> Table:
        return self.process()


class ImportJSON(Import):
    def __init__(self, filename: str, key: Optional[str] = None):
        super().__init__(filename)
        self.key = key

    def process(self) -> Table:
        with open(self.filename) as json_file:
            data = json.load(json_file)
        if self.key is not None:
            data = data[self.key]
        result = Table(list(data[0].keys()))
        for item in data:
            result.append_row(item.values())
        return result

    def transform(self) -> Table:
        return self.process()
