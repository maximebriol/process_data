from .table import Table
from .abc import AbstractTransformer
import datetime

class FenetrageTransformer(AbstractTransformer):
    def fenetrage(self,duree:int,fin:date,table:Table):
        date_fin=datetime.datetime.strtime(fin,"%m/%d/%y")
        date_debut=date_fin-datetime.timetimedelta(days=duree)
        col_jours=table.get_column("Jour")
        for i in range(0,len(col_jours)):
            if datetime.datetime.strtime(col_jours,"%m/%d/%y")>date_fin or datetime.datetime.strtime(col_jours,"%m/%d/%y")<date_debut:
                table.remove(i)
        return table