from ... import data
from ..cast import Cast
from ..date import Date
from ..moving_average import MovingAverage
from ..importation import CSVReader
from ..select import Select


def test_importation():
    covid = CSVReader(str(data.covid_incid_reg()))
    table = covid.process()

    table = Date(dict(jour="%Y-%m-%d")).process(table)
    table = Cast(dict(numReg=int, incid_rea=float)).process(table)

    transformer = MovingAverage(3, "incid_rea", "jour").process(table)