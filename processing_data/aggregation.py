from typing import Any, List, Optional
from .table import Table
from .abc import AbstractTransformer

# def _zip(items:List[List[Any]]):
#     result = [[] * len(items)]
#     index = 0
#     while index < len(items):
#         for ix in range(len(items)):
#             result[index].append(items[ix][index])
#         index += 1
#     return result


class Operators:
    def __init__(self) -> None:
        self.values = []

    def append(self, value: Any) -> None:
        self.values.append(value)

    def mean(self) -> float:
        return sum(self.values) / len(self.values)

    def min(self) -> float:
        return min(self.values)

    def max(self) -> float:
        return max(self.values)


class Aggregation(AbstractTransformer):
    def __init__(self, on: List[str], operator: Optional[str] = None) -> None:
        self.on = on
        self.operator = operator or "mean"

    def process(self, table: Table) -> Table:
        # Index des colonnes agrégéee.
        indices = [table.columns.get_index(item) for item in self.on]
        # Index des colonnes traitées
        column_indices = list(set(range(table.ncolumns())) - set(indices))
        aggregators = dict()
        # Dictionnaire entre l'ensemble des valeurs distinctes de la colonne
        # agrégée et les agrégateurs des différentes colonnes traitées.
        column_values = tuple(
            zip(*(table.get_column(name) for name in self.on)))
        # Dictionnaire entre l'ensemble des valeurs distinctes de la colonne
        # agrégée et les agrégateurs des différentes colonnes traitées.
        for item in column_values:
            if item in aggregators:
                continue
            # aggregators[item] = []
            # for column in columns:
            #     aggregators[item].append(agregation.Agregation())
            aggregators[item] = [Operators() for _ in column_indices]
        # Pour toutes les lignes de la table
        for ix in range(table.nrows()):
            # Lecture de la ligne courante
            row = table.get_row(ix)
            # Lecture de la valeur agrégée
            value = tuple(row[ix] for ix in indices)
            # Agrégateur de cette valeur
            agg = aggregators[value]
            # Pour toutes les colonnes traitées
            for ix, index in enumerate(column_indices):
                # On ajoute la valeur de la colonne à l'agrégateur
                agg[ix].append(row[index])

        # Construction de la table résultat
        result = Table(self.on +
                       [table.columns.get_name(ix) for ix in column_indices])
        # Pour toutes les valeurs agrégées
        for item, values in aggregators.items():
            # On ajoute, la valeur agrégée, les valeurs de l'opérateur
            # sélectionnée pour toutes les colonnes traitées
            result.append_row(
                list(item) + [getattr(agg, self.operator)() for agg in values])
        return result

    def transform(self, table: Table) -> Table:
        return self.process(table)
