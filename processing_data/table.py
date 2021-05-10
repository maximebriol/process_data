from typing import Any, List, Dict
from .column import Columns
from .matrix import Matrix


def _insert(position: int, items: List[Any], item: Any) -> None:
    """Insérer une nouvelle colonne à la position demandée.
    position doit être compris dans l'intervalle [0, len(items) - 1]
    """
    if not items:
        raise ValueError("Impossible d'insérer un élement dans une liste vide")
    if position not in range(len(items)):
        raise ValueError(f"{position} doit être dans l'intervalle "
                         f"[0, {len(items) - 1}]")
    items.insert(position, item)

class Table:
    def __init__(self, columns: List[str]):
        self.columns = Columns(
            columns)  #toutes les colonnes ou juste nom des variables
        self.matrix = Matrix(nrows=0, ncolumns=self.columns.get_length())

    def nrows(self) -> int:
        return self.matrix.nrows()

    def ncolumns(self) -> int:
        return self.matrix.ncolumns()

    def get_column(self, name: str) -> List[Any]:
        return self.matrix.get_column(self.columns.get_index(name))

    def get_row(self, index: int) -> List[Any]:
        return self.matrix.get_row(index)

    def add_column(self, name: str, position: int, items: List[Any]):
        if len(items) != self.nrows():
            raise ValueError(f"le nombre de lignes {len(items)} "
                             f"est différent de celui attendu {self.nrows}")
        self.columns.insert(name, position)
        self.matrix.add_column(position, items)

    def append_column(self, name: str, items: List[Any]):
        nrows = self.nrows()
        #Si la matrice est vide, on ne vérifie rien.
        if nrows != 0 and self.ncolumns() != 0:
            if len(items) != self.nrows():
                raise ValueError(
                    f"le nombre de lignes {len(items)} "
                    f"est différent de celui attendu {self.nrows()}")
        self.columns.append(name)
        self.matrix.append_column(items)

    def add_row(self, position: int, items: List[Any]):
        self.matrix.add_row(position, items)

    def append_row(self, items: List[Any]):
        self.matrix.append_row(items)

    def remove_column(self, name: str):
        position = self.columns.get_index(name)
        self.matrix.remove_column(position)
        self.columns.remove(name)

    def remove_row(self, position: int):
        self.matrix.remove_row(position)

    def column_names(self) -> List[str]:
        column_name = []
        for item in range(self.columns.get_length()):
            column_name.append(self.columns.get_name(item))
        return column_name

    def select_columns(self, columns: List[str]) -> "Table":
        column_index = [self.columns.get_index(item) for item in columns]
        result = Table(
            [self.columns.get_name(index) for index in column_index])
        for ix in range(self.nrows()):
            row = self.get_row(ix)
            # new_row = []
            # for index in column_index:
            #     new_row.append(row[index])
            # result.append_row(new_row)
            result.append_row([row[index] for index in column_index])
        return result

    def select_values(self, column: Dict[str, Any]) -> "Table":
        indices = set()
        for name, value in column.items():
            column_indices = set()
            index = self.columns.get_index(name)
            for ix, item in enumerate(self.matrix.get_column(index)):
                if item == value:
                    column_indices.add(ix)
            if indices:
                indices = indices & column_indices
            else:
                indices = column_indices
        result = Table(self.columns.columns())
        for ix in sorted(indices):
            result.append_row(self.get_row(ix))
        return result

    def join(self, other: "Table", on: str) -> "Table":
        try:
            index_other = other.columns.get_index(on)
        except ValueError:
            raise ValueError(f"la colonne {on} n'existe pas dans other")

        values = self.get_column(on)
        values_other = other.get_column(on)
        columns_other = other.column_names()
        del columns_other[index_other]
        result = Table(self.column_names() + columns_other)
        for ix, item in enumerate(values):
            row = self.get_row(ix)
            try:
                ix_other = values_other.index(item)
                row_other = other.get_row(ix_other)
                del row_other[index_other]
                result.append_row(row + row_other)
            except ValueError:
                # row_other = [None] * (other.columns.get_length() - 1)
                pass
        return result
