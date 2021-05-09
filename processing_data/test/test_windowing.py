import datetime
import pathlib
from ..date import Date
from ..importation import ImportCSV
from ..windowing import Windowing


def test_importation():
    path = pathlib.Path(__file__).parent.joinpath(
        'covid-hospit-incid-reg-2021-03-03-17h20.csv')

    covid = ImportCSV(str(path))
    table = covid.transform()

    date = Date("%Y-%m-%d", "jour")
    table = date.transform(table)

    wind = Windowing("jour", datetime.datetime(2020, 3, 20),
                     datetime.datetime(2020, 3, 20, 23, 59, 59, 999999))
    table = wind.process(table)
    assert table.nrows() == 18