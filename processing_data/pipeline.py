from typing import List, Optional
from .abc import AbstractOperation
from .table import Table


class Pipeline:
    def __init__(self):
        self.steps: List[AbstractOperation] = []

    def add_step(self, step: AbstractOperation) -> "Pipeline":
        self.steps.append(step)
        return self

    def clear(self) -> None:
        self.steps.clear()

    def run(self, table: Optional[Table] = None) -> Table:
        if table is None:
            result = Table([])
        else:
            result = table.copy()
        for item in self.steps:
            result = item.process(result)
        return result