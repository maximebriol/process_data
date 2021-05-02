import abc
from .table import Table


class AbstractOperation(abc.ABC):
    @abc.abstractmethod
    def process(self, table: Table) -> Table:
        ...


class AbstractTransformer(AbstractOperation):
    def process(self, table: Table) -> Table:
        ...

    @abc.abstractmethod
    def transform(self, table: Table) -> Table:
        ...


class AbstractEstimator(AbstractOperation):
    def process(self, table: Table) -> Table:
        ...

    @abc.abstractmethod
    def fit(self, table: Table) -> Table:
        ...
