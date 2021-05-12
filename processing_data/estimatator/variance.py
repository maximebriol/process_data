from typing import Any, List
from ..table import Table
from .abc import AbstractEstimator


class Variance(AbstractEstimator):
    def process(self, table: Table) -> Table:
        column_names = table.column_names()
        # On récupère le nom de toutes les colonnes.
        result = Table(column_names)
        #On crée une table en mettant en paramètre le nom des colonnes précédentes.
        row = []
        for name in column_names:
            row.append(self.calculate(table.get_column(name)))
            #On calcule la variance pour toutes les variables de la table.
        result.append_row(row)
        return result

    def fit(self, table: Table) -> Table:
        return self.process(table)

    @staticmethod
    def calculate(values: List[Any]) -> float:
        mean_square = 0
        # On initialise la moyenne des carrés à 0.
        for ix in range(len(values)):
            mean_square += (values[ix] * values[ix]) / len(values)
            #On calcule la moyenne des carrés.
        return mean_square - (sum(values) / len(values)) * (sum(values) /
                                                            len(values))
                                                            #On retourne la variance.
