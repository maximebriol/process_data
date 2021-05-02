from .abc import AbstractTransformer
from .table import Table


class MovingAverageTransformer(AbstractTransformer):
    def transform(self, table: Table) -> Table:
        ...
