from typing import List, Any

class Insert:
    def _insert(self, position: int, items: List[Any], item: Any) -> None:
        """Insérer une nouvelle colonne à la position demandée.
        position doit être compris dans l'intervalle [0, len(items) - 1]
        """
        if not items:
            raise ValueError("Impossible d'insérer un élement dans une liste vide")
        if position not in range(len(items)):
            raise ValueError(f"{position} doit être dans l'intervalle "
                            f"[0, {len(items) - 1}]")
        items.insert(position, item)