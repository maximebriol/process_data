import datetime
from ... import data
from ..importation import CSVReader, JSONReader
from ..date import Date


def test_importation():
    covid = CSVReader(str(data.covid_incid_reg()))
    tableau = covid.process()

    date = Date(dict(jour="%Y-%m-%d"))
    tableau = date.process(tableau)
    values = tableau.get_column("jour")
    assert isinstance(values[0], datetime.datetime)

    hollidays = JSONReader(str(data.school_holidays()), 'Calendrier')
    tableau = hollidays.process()
