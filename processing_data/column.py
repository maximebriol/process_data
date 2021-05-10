from typing import List, Any


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