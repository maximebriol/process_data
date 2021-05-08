import pathlib
from ..importation import Importation


def test_Importation():
    path = pathlib.Path(__file__).parent.joinpath(
        'covid-hospit-incid-reg-2021-03-03-17h20.csv')
    CovidTable = Importation('', str(path))
    tableau=CovidTable.import_csv('', str(path))
    