import pathlib
from .table import Columns, Table
from .importation import Importation


class Agregation:
    def __init__(self, echelle: str, table: "Table") -> "Table":
        self.echelle = echelle
        self.table = table

    def agregation(self, echelle_debut: str, echelle_fin: str,
                   table: "Table") -> "Table":
        table_agreg = Table(
            self.table.column_name()
        )  #On donne à la nouvelle table les mêmes variables qu'à la tbale initiale
        table_agreg.remove_column(
            echelle_debut
        )  #On retire la variable d'échelon géorgaphique de base
        path = pathlib.Path(__file__).parent.joinpath(
            'departements_regions_france_2016.csv')
        #On importe la table des correspondances départements-régions
        Correspondances = Importation('', str(path))
        Correspondances.import_csv('', str(path))
        Correspondances[1]
        

        table_agreg.add_column(name, position, items)