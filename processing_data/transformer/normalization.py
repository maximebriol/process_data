from .. import estimatator
from ..table import Table
from .abc import AbstractTransformer


class Normalization(AbstractTransformer):
    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])
        for name in names:
            values = table.get_column(name)
            # skip non numeric data
            if all(isinstance(item, (int, float)) for item in values):
                variance = estimatator.Variance.calculate(values)
                mean = estimatator.Mean.calculate(values)
                for ix in range(len(values)):
                    values[ix] = (values[ix] - mean) / (variance)**(0.5)
            result.append_column(name, values)
        return result
