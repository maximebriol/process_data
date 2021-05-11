import datetime
from ...table import Table
from ..select import Select


def test_select_values():
    table = Table(["a", "b", "c", "d"])

    table.append_row(
        [datetime.date(2020, 3, 19), "Auvergne-Rhône-Alpes", 84, 44])
    table.append_row(
        [datetime.date(2020, 3, 19), "Bourgogne-Franche-Comté", 27, 33])
    table.append_row([datetime.date(2020, 3, 19), "Bretagne", 53, 8])
    table.append_row(
        [datetime.date(2020, 3, 19), "Centre-Val de Loire", 24, 6])
    table.append_row([datetime.date(2020, 3, 19), "Corse", 94, 11])
    table.append_row([datetime.date(2020, 3, 19), "Grand-Est", 44, 69])
    table.append_row([datetime.date(2020, 3, 19), "Guadeloupe", 1, 0])
    table.append_row([datetime.date(2020, 3, 19), "Guyane", 3, 0])
    table.append_row([datetime.date(2020, 3, 19), "Hauts-de-France", 32, 37])
    table.append_row([datetime.date(2020, 3, 19), "Ile-de-France", 11, 151])
    table.append_row([datetime.date(2020, 3, 19), "La Réunion", 4, 0])
    table.append_row([datetime.date(2020, 3, 19), "Martinique", 2, 0])
    table.append_row([datetime.date(2020, 3, 19), "Mayotte", 6, 0])
    table.append_row([datetime.date(2020, 3, 19), "Normandie", 28, 7])
    table.append_row([datetime.date(2020, 3, 19), "Nouvelle-Aquitaine", 75, 7])
    table.append_row([datetime.date(2020, 3, 19), "Occitanie", 76, 29])
    table.append_row([datetime.date(2020, 3, 19), "Pays de la Loire", 52, 11])
    table.append_row(
        [datetime.date(2020, 3, 19), "Provence-Alpes-Côte d'Azur", 93, 25])
    table.append_row(
        [datetime.date(2020, 3, 20), "Auvergne-Rhône-Alpes", 84, 16])
    table.append_row(
        [datetime.date(2020, 3, 20), "Bourgogne-Franche-Comté", 27, 9])
    transformer = Select(dict(a=datetime.date(2020, 3, 19)))
    a = transformer.process(table)
    assert a.nrows() == table.nrows() - 2
    transformer = Select(
        dict(dict(a=datetime.date(2020, 3, 19), b="Occitanie")))
    a = transformer.process(table)
    assert a.nrows() == 1