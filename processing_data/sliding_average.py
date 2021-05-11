from .table import Table
from .date import Date
from .abc import AbstractTransformer

class SlidingAverage(AbstractTransformer):
    def process(self, table: Table, month: int, slide: int) -> Table:
        
