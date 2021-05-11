import abc
from typing import Any, List
from ..abc import AbstractOperation
from ..table import Table


class AbstractEstimator(AbstractOperation):
    def process(self, table: Table) -> Table:
        ...

    @abc.abstractmethod
    def fit(self, table: Table) -> Table:
        ...

    @staticmethod
    @abc.abstractmethod
    def calculate(*args) -> Any:
        ...