from typing import List
from .abc import AbstractOperation
from .table import Table


class Pipeline:
    def __init__(self):
        self.steps: List[AbstractOperation] = []

    def add_step(self, step: AbstractOperation) -> None:
        self.steps.append(step)

    def run(self, table: Table) -> Table:
        ...
