import datetime
from ... import data
from ..date import Date
from ..importation import CSVReader
from ..windowing import Windowing


def test_windowing():
    
    covid = CSVReader(str(data.covid()))
    table = covid.process()

    date = Date(dict(jour="%Y-%m-%d"))
    table = date.process(table)

    wind = Windowing("jour", datetime.datetime(2020, 3, 20),
                     datetime.datetime(2020, 3, 20, 23, 59, 59, 999999))
    table = wind.process(table)
    assert table.nrows() == 18