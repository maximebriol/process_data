from typing import Any, List


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


class Columns:
    """Gère la liste des colonnes d'une table"""
    def __init__(self, columns: List[str]) -> None:
        self._columns = [item for item in columns]

    def columns(self) -> List[str]:
        return [item for item in self._columns]

    def get_index(self, name: str) -> int:
        """Obtenir l'index de la colonne"""
        return self._columns.index(name)

    def get_name(self, index: int) -> str:
        """Obtenir le nom de la colonne"""
        return self._columns[index]

    def remove(self, name: str) -> None:
        """Suppimer la colonne 'name'"""
        idx = self.get_index(name)
        del self._columns[idx]

    def get_length(self) -> int:
        """Obtenir le nombre de colonnes"""
        return len(self._columns)

    def assert_not_exists(self, name: str) -> None:
        """S'assurer que la colonne 'name' n'existe"""
        if name in self._columns:
            raise ValueError(f"la colonne {name} existe déjà")

    def insert(self, name: str, position: int) -> None:
        """Insérer une nouvelle colonne à la position demandée.
        position doit être compris dans l'intervalle [0, get_length() - 1]
        """
        self.assert_not_exists(name)
        _insert(position, self._columns, name)

    def append(self, name: str) -> None:
        """Ajouter la colonne 'name'"""
        self.assert_not_exists(name)
        self._columns.append(name)


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

    def remove_column(self, position: int):
        del self.matrix[position]

    def remove_row(self, position: int):
        for jx in range(self.ncolumns()):
            del self.matrix[jx][position]


class Table:
    def __init__(self, columns: List[str]):
        self.columns = Columns(columns)
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
