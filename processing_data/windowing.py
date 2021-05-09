from .table import Table
from .abc import AbstractTransformer
import datetime


class Windowing(AbstractTransformer):
    def __init__(self, on: str, first: datetime.datetime,
                 last: datetime.datetime) -> None:
        super().__init__()
        self.on = on
        self.first = first
        self.last = last

    def process(self, table: Table) -> Table:
        result = Table(table.column_names())
        index = table.columns.get_index(self.on)
        for ix in range(table.nrows()):
            row = table.get_row(ix)
            value = row[index]
            if self.first <= value <= self.last:
                result.append_row(row)
        return result

    def transform(self, table: Table) -> Table:
        return self.process(table)
