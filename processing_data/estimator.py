from .abc import AbstractTransformer
from .table import Table


class MeanEstimator(AbstractTransformer):
    def fit(self, table: Table) -> Table:
        ...
