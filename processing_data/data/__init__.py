import pathlib


def covid() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath(
        "covid-hospit-incid-reg-2021-03-03-17h20.csv")


def school_holidays() -> pathlib.Path:
    return pathlib.Path(__file__).parent.joinpath("VacancesScolaires.json")