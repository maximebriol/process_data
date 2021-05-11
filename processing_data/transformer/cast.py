from typing import Dict
import datetime
from .abc import AbstractTransformer
from ..table import Table


class Cast(AbstractTransformer):
    def __init__(self, columns: Dict[str, type]) -> None:
        super().__init__()
        self.columns = columns

    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])

        for name in names:
            col = table.get_column(name)
            if name in self.columns:
                cast = self.columns[name]
                col = [cast(item) for item in col]
            result.append_column(name, col)
        return result
