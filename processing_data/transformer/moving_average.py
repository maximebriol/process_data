from typing import List, Any
import datetime
from ..estimatator import Mean
from ..table import Table
from .abc import AbstractTransformer
from .windowing import Windowing


def assert_is_sorted(values: List[Any], ascending: bool) -> None:
    if len(values) == 0:
        raise ValueError("Impossible de traiter un liste vide")
    for i in range(1, len(values)):
        if ascending and values[i - 1] > values[i]:
            raise ValueError("La liste n'est triée dans l'ordre croissant")
        if not ascending and values[i - 1] < values[i]:
            raise ValueError("La liste n'est triée dans l'ordre décroissant")


class MovingAverage(AbstractTransformer):
    def __init__(self,
                 period: int,
                 on: str,
                 date: str,
                 ascending: bool = True):
        self.ascending = ascending
        self.period = datetime.timedelta(days=period)
        self.date = date
        self.on = on

    def process(self, table: Table) -> Table:
        mean = []
        dates = table.get_column(self.date)
        assert_is_sorted(dates, self.ascending)

        for i in range(table.nrows()):
            last_date = dates[i]
            first_date = last_date - self.period
            if first_date < dates[0]:
                mean.append(float('nan'))
            else:
                subset = Windowing(self.date, first_date,
                                   last_date).process(table)
                # selectionne que la variable que l'on veut
                column = subset.get_column(self.on)
                mean.append(Mean.calculate(column))
        table.set_column(self.on, mean)
        return table
