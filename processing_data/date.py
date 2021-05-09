import datetime
from .abc import AbstractTransformer
from .table import Table


class Date(AbstractTransformer):
    def __init__(self, format: str, on: str) -> None:
        super().__init__()
        self.format = format
        self.on = on

    def process(self, table: Table) -> Table:
        result = Table(table.column_names())
        index = table.columns.get_index(self.on)

        for ix in range(table.nrows()):
            row = table.get_row(ix)
            row[index] = datetime.datetime.strptime(row[index], self.format)
            result.append_row(row)
        return result

    def transform(self, table: Table) -> Table:
        return self.process(table)
