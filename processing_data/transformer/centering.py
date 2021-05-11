from ..estimatator import Mean
from ..table import Table
from .abc import AbstractTransformer


class Centering(AbstractTransformer):
    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])
        for name in names:
            values = table.get_column(name)
            # skip non numeric data
            if all(isinstance(item, (int, float)) for item in values):
                mean = Mean.calculate(values)
                for ix in range(len(values)):
                    values[ix] -= mean
            result.append_column(name, values)
        return result
