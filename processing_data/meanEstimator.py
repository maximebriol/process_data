from .table import Table
from .abc import AbstractEstimator

class MeanEstimator(AbstractEstimator):
    def mean(self, table :"Table",name_column: str)->float:# je comprends pas pourquoi ya une erreur
            """Calcul de la moyenne d'une colonne 
            
            Parameters
            --------
            column:list
                colonne sur laquelle on veut calculer la moyenne de ses valeurs
            
            Returns
            -------
            float
                la moyenne des valeurs de la colonne
            
            Examples
            -------
            >>>mean([1,3,4,5,0])
            2.6
            """
            liste=table.get_column(name_column)
            s=0
            for i in range(len(liste)):
                s+=liste[i]
            return s/len(liste)