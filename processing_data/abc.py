import abc
from .table import Table


class AbstractOperation(abc.ABC):
    @abc.abstractmethod
    def process(self, table: Table) -> Table:
        ...


