from typing import Any, Dict
from ..table import Table
from .abc import AbstractTransformer


class Select(AbstractTransformer):
    def __init__(self, column: Dict[str, Any]) -> None:
        super().__init__()
        self.column = column

    def process(self, table: Table) -> Table:
        indices = set()
        for name, value in self.column.items():
            column_indices = set()
            for ix, item in enumerate(table.get_column(name)):
                if item == value:
                    column_indices.add(ix)
            if indices:
                indices = indices & column_indices
            else:
                indices = column_indices
        result = Table(table.columns.columns())
        for ix in sorted(indices):
            result.append_row(table.get_row(ix))
        return result
