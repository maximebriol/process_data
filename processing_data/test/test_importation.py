import datetime
import pathlib
from ..importation import ImportCSV, ImportJSON
from ..date import Date


def test_importation():
    path = pathlib.Path(__file__).parent.joinpath(
        'covid-hospit-incid-reg-2021-03-03-17h20.csv')
    covid = ImportCSV(str(path))
    tableau = covid.process()

    date = Date("%Y-%m-%d", "jour")
    tableau = date.transform(tableau)
    values = tableau.get_column("jour")
    assert isinstance(values[0], datetime.datetime)

    path = pathlib.Path(__file__).parent.joinpath('VacancesScolaires.json')
    hollidays = ImportJSON(str(path), 'Calendrier')
    tableau = hollidays.process()
