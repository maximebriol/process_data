from typing import List, Any
from .column import Columns

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

class Matrix:
    def __init__(self, nrows: int, ncolumns: int) -> None:
        self.matrix = []
        for jx in range(ncolumns):
            # Ajouter les lignes
            rows = []
            for ix in range(nrows):
                rows.append(None)
            # On ajoute les lignes à la colonne i
            self.matrix.append(rows)

    def __repr__(self) -> str:
        return str(self.matrix)

    def nrows(self) -> int:
        if len(self.matrix) == 0:
            return 0
        return len(self.matrix[0])

    def ncolumns(self) -> int:
        return len(self.matrix)

    def get_item(self, row: int, column: int):
        # Retourne le coefficient situé à la ligne row et à la colonne column
        return self.matrix[column][row]

    def get_column(self, column: int) -> List[Any]:
        # result = []
        # for item in self.matrix:
        #     result.append(item)
        # return result
        return [item for item in self.matrix[column]]

    def get_row(self, row: int) -> List[Any]:
        # result = []
        # for jx in range(self.ncolumns):
        #     result.append(self.matrix[jx][row])
        # return result
        return [self.matrix[jx][row] for jx in range(self.ncolumns())]

    def set_item(self, row: int, column: int, item: Any):
        # Retourne le coefficient situé à la ligne row et à la colonne column
        self.matrix[column][row] = item

    def set_column(self, column: int, items: List[Any]):
        if len(items) != self.nrows():
            raise ValueError(
                f"le nombre de lignes {len(items)} est différent de celui "
                f"attendu: {self.nrows()}")
        if column not in range(self.ncolumns()):
            raise ValueError(f"la colonne {column} n'existe pas")

        self.matrix[column] = [item for item in items]

    def set_row(self, row: int, items: List[Any]):
        if len(items) != self.ncolumns():
            raise ValueError(
                f"le nombre de colonnes {len(items)} est différent de celui "
                f"attendu: {self.ncolumns()}")
        if row not in range(self.nrows()):
            raise ValueError(f"la ligne {row} n'existe pas")
        for jx in range(self.ncolumns()):
            self.matrix[jx][row] = items[jx]

    def add_column(self, position: int, items: List[Any]):
        _insert(position, self.matrix, None)
        try:
            self.set_column(position, items)
        except ValueError:
            del self.matrix[position]
            raise

    def add_row(self, position: int, items: List[Any]):
        for jx in range(self.ncolumns()):
            _insert(position, self.matrix[jx], None)
        try:
            self.set_row(position, items)
        except ValueError:
            for jx in range(self.ncolumns()):
                del self.matrix[jx][position]
            raise

    def append_row(self, items: List[Any]):
        if len(items) != self.ncolumns():
            raise ValueError(
                f"le nombre de colonnes {len(items)} est différent de celui "
                f"attendu: {self.ncolumns()}")
        for jx, item in enumerate(items):
            self.matrix[jx].append(item)

    def append_column(self, items: List[Any]):
        if self.nrows() != 0:
            if len(items) != self.nrows():
                raise ValueError(
                    f"le nombre de ligne {len(items)} est différent de celui "
                    f"attendu: {self.nrows()}")
        self.matrix.append(items)

    def remove_column(self, position: int):
        del self.matrix[position]

    def remove_row(self, position: int):
        for jx in range(self.ncolumns()):
            del self.matrix[jx][position]