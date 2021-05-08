from .table import Table
from .abc import AbstractTransformer

class NormalisationTransformer(AbstractTransformer) :
    def __init__(self, table: "Table"):
        self.table =table

    def normalisation(self, table: "Table"):
            """Normaliser les colonnes d'un tableau de valeurs
            
            Parameters
            --------
            table : list(list)
                tableau de valeurs dont les colonnes sont à normaliser
            
            Returns
            ------
            list(list)
                retourne un tableau 
            ...
            
            """
            for self.column in range(self.table.ncolumns()) : 
                for i in range(0, len(self.column)):
                    self.column[i] = self.column[i]-self.column.MeanEstimator.mean()
            return table.ncolumns() #on retourne pas column ?