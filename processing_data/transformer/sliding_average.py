from ..table import Table
from .date import Date
from .abc import AbstractTransformer
from .windowing import Windowing
from typing import List, Any

class MovingAverage(AbstractTransformer):
    def __init__(self,period, variable):
        self.period = period
        self.variable = variable

    def transform(self, table : Table)-> List:
        self.index = table.get_index(self.variable)
        mean = [] #listevide
        colonne = table.get_column(self.variable)
        date = table.get_column(jour)
        date_maximale = date[len(date)-1]
        date_minimale = date[0]
        
        for i in range(table.nrows()):
            date_fin = datetime.datetime.strptime(date[i], "%y/%m/%d")
            date_debut = date_fin - datetime.timedelta(days=period)
            if date_debut < date_minimale : 
                mean.append('NA')
            else :
                window =Windowing()
                window = table.Windowing(jour,date_debut, date_fin)  # fenetrage 
                colonne = window.get_column(self.variable) #selectionne que la variable que l'on veut
                mean.append(mean_estimator.MeanEstimator(colonne))
        return mean 
