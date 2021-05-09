from .table import Table
from .abc import AbstractTransformer
from .mean_estimator import MeanEstimator


class CentrageTransformer(AbstractTransformer):
    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])
        for position, name in enumerate(names):
            values = table.get_column(name)
            mean = MeanEstimator.mean(values)
            for ix in range(len(values)):
                values[ix] -= mean
            result.add_column(name, position, values)
        return result

    def transform(self, table: Table) -> Table:
        return self.process(table)
