from ..estimatator import Mean
from ..table import Table
from .abc import AbstractTransformer


class Centering(AbstractTransformer):
    def process(self, table: Table) -> Table:
        names = table.column_names()
        #On copie les noms des variables
        result = Table([])
        for name in names:
            values = table.get_column(name)
            #On récupère les valeurs de chaque colonne
            # skip non numeric data
            if all(isinstance(item, (int, float)) for item in values):
                mean = Mean.calculate(values)
                #On récupère les moyennes de chaque variable
                for ix in range(len(values)):
                    #On enlève pour chaque observation la moyenne de la variable à laquelle elle appartient.
                    values[ix] -= mean
            result.append_column(name, values)
        return result
