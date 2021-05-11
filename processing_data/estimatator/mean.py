from typing import Any, List
import datetime
from ..table import Table
from .abc import AbstractEstimator


class Mean(AbstractEstimator):
    def process(self, table: Table) -> Table:
        column_names = table.column_names()
        result = Table(column_names)
        row = []
        for name in column_names:
            row.append(self.calculate(table.get_column(name)))
        result.append_row(row)
        return result

    def fit(self, table: Table) -> Table:
        return self.process(table)

    @staticmethod
    def calculate(values: List[Any]) -> Any:
        if len(values) and isinstance(values[0], datetime.datetime):
            epoch = datetime.datetime(1970, 1, 1)
            values = [(item - epoch).total_seconds() for item in values]
            return datetime.datetime.utcfromtimestamp(
                sum(values) / len(values))
        return sum(values) / len(values)
