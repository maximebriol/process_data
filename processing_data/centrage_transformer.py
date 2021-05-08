from .table import Table
from .abc import AbstractTransformer

class CentrageTransformer(AbstractTransformer):
    def __init__(self, table: Table):
        self.table = table

    def centrage(self, table : Table) -> "Table":
            """Centrer les colonnes d'un tableau de valeurs
            
            Parameters
            --------
            table : list(list)
                tableau de valeurs dont les colonnes sont à centrer
            
            Returns
            ------
            list(list)
                retourne un tableau 
            ...
            
            """
            self.table.NormalisationTransformer.normalisation()
            for column in self.table.ncolumns():
                for i in range(O, len(column)):
                    column[i] = column[i]/sqrt(column.VarianceEstimator())
            return self.table.ncolumns() 
        