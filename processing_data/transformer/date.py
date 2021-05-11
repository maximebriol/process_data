from processing_data import column
from typing import Dict
import datetime
from .abc import AbstractTransformer
from ..table import Table


class Date(AbstractTransformer):
    def __init__(self, columns: Dict[str, str]) -> None:
        super().__init__()
        self.columns = columns

    def process(self, table: Table) -> Table:
        names = table.column_names()
        result = Table([])

        for name in names:
            col = table.get_column(name)
            if name in self.columns:
                format = self.columns[name]
                for ix, item in enumerate(col):
                    # Ignore les données invalides
                    try:
                        col[ix] = datetime.datetime.strptime(item, format)
                    except TypeError:
                        pass
            result.append_column(name, col)
        return result
