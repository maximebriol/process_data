from typing import Any, List
from .table import Table
from .abc import AbstractEstimator
from .mean_estimator import MeanEstimator

class VarianceEstimator(AbstractEstimator):
    def process(self, table: Table) -> Table:
        column_names = table.column_names()
        result = Table(column_names)
        row = []
        for name in column_names:
            row.append(self.variance(table.get_column(name)))
        result.append_row(row)
        return result

    def fit(self, table: Table) -> Table:
        return self.process(table)

    @staticmethod
    def variance(values: List[Any]) -> float:
        moy_carre = 0
        for ix in range(len(values)):
            moy_carre += (values[ix] * values[ix]) / len(values)
        return moy_carre - (sum(values) / len(values)) * (sum(values) / len(values))
