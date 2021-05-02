from .abc import AbstractTransformer
from .table import Table


class MeanEstimator(AbstractTransformer):
    def fir(self, table: Table) -> Table:
        ...
