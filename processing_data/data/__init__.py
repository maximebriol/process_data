import pathlib


def covid_incid_reg() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "covid-hospit-incid-reg-2021-03-03-17h20.csv")


def covid_age() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv")


def covid() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "donnees-hospitalieres-covid19-2021-03-03-17h03.csv")


def covid_hospitals() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "donnees-hospitalieres-etablissements-covid19-2021-03-03-17h03.csv")


def covid_new() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")


def school_holidays() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath("VacancesScolaires.json")


def region() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath("region2020.csv")