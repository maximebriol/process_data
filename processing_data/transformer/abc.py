import abc
from ..abc import AbstractOperation
from ..table import Table


class AbstractTransformer(AbstractOperation):
    @abc.abstractmethod
    def process(self, table: Table) -> Table:
        ...
