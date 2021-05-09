from typing import Any, List
from .table import Table
from .abc import AbstractEstimator


class MeanEstimator(AbstractEstimator):
    def process(self, table: Table) -> Table:
        column_names = table.column_names()
        result = Table(column_names)
        row = []
        for name in column_names:
            row.append(self.mean(table.get_column(name)))
        result.append_row(row)
        return result

    def fit(self, table: Table) -> Table:
        return self.process(table)

    @staticmethod
    def mean(values: List[Any]) -> float:
        return sum(values) / len(values)
