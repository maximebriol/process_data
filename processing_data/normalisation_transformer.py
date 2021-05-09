from .table import Table
from .abc import AbstractTransformer
from .variance_estimator import VarianceEstimator

class NormalizationTransformer(AbstractTransformer) :
    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])
        for name in names:
            values = table.get_column(name)
            variance = VarianceEstimator.variance(values)
            for ix in range(len(values)):
                values[ix] = values[ix]/ (variance)**(0.5)
            result.append_column(name, values)
        return result

    def transform(self, table: Table) -> Table:
        return self.process(table)