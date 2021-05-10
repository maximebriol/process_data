import pytest
import datetime
from ..column import Columns
from ..matrix import Matrix
from ..table import Table


def test_columns():
    columns = ["A", "B", "C"]
    obj = Columns(columns)

    assert obj.columns() == columns
    assert id(obj.columns()) != id(columns)
    assert obj.get_index("B") == 1
    assert obj.get_name(1) == "B"
    assert obj.get_length() == 3

    obj.remove("A")
    assert obj.get_index("B") == 0
    assert obj.get_name(0) == "B"
    assert obj.get_length() == 2

    obj.append("A")
    assert obj.get_length() == 3
    assert obj.get_index("A") == 2
    assert obj.get_name(2) == "A"

    with pytest.raises(ValueError):
        obj.append("A")

    obj.insert("D", 2)
    assert obj.get_length() == 4
    assert obj.get_index("A") == 3
    assert obj.get_index("D") == 2
    assert obj.get_name(2) == "D"

    with pytest.raises(ValueError):
        obj.insert("X", -1)

    with pytest.raises(ValueError):
        obj.insert("X", 4)


def test_matrix():
    matrix = Matrix(2, 3)
    assert matrix.nrows() == 2
    assert matrix.ncolumns() == 3
    matrix.set_column(0, [0, 10])
    matrix.set_column(1, [1, 11])
    matrix.set_column(2, [2, 12])
    for ix in range(matrix.nrows()):
        for jx in range(matrix.ncolumns()):
            assert matrix.get_item(ix, jx) == ix * 10 + jx

    matrix.set_row(0, [10, 20, 30])
    assert matrix.get_column(1) == [20, 11]
    assert matrix.get_row(1) == [10, 11, 12]
    matrix.append_row([20, 21, 22])
    assert matrix.get_column(1) == [20, 11, 21]
    assert matrix.get_row(1) == [10, 11, 12]
    assert matrix.get_row(2) == [20, 21, 22]
    matrix.remove_column(1)
    assert matrix.ncolumns() == 2
    assert matrix.nrows() == 3
    assert matrix.get_row(1) == [10, 12]
    matrix.remove_row(1)
    assert matrix.ncolumns() == 2
    assert matrix.nrows() == 2
    assert matrix.get_row(1) == [20, 22]

    with pytest.raises(ValueError):
        matrix.set_column(-1, [0, 1])

    with pytest.raises(ValueError):
        matrix.set_column(1, [0, 2, 2])

    with pytest.raises(ValueError):
        matrix.set_row(1, [0, 2, 2])

    with pytest.raises(ValueError):
        matrix.set_row(-1, [0, 1])

    assert matrix.get_item(0, 1) == 30
    matrix.set_item(0, 1, 20)
    assert matrix.get_item(0, 1) == 20


def test_table():
    table = Table(["A", "B", "C"])
    table.append_row([0, 1, 2])
    table.append_row([10, 20, 30])
    table.append_row([20, 30, 40])
    table.append_row([30, 40, 50])
    assert table.nrows() == 4
    assert table.ncolumns() == 3
    assert table.get_column("B") == [1, 20, 30, 40]
    assert table.get_row(2) == [20, 30, 40]
    assert table.column_names() == ["A", "B", "C"]
    table.remove_column("B")
    assert table.ncolumns() == 2
    assert table.nrows() == 4
    assert table.get_row(2) == [20, 40]
    with pytest.raises(ValueError):
        table.get_column("B")
    table.add_column("D", 1, [4, 5, 6, 7])
    assert table.ncolumns() == 3
    assert table.get_row(2) == [20, 6, 40]
    table.add_row(2, [9, 8, 7])
    assert table.nrows() == 5
    assert table.ncolumns() == 3
    assert table.get_column("D") == [4, 5, 8, 6, 7]
    with pytest.raises(ValueError):
        table.add_column("A", 0, [0, 1, 2, 3, 4])
    with pytest.raises(ValueError):
        table.add_column("X", 0, [1, 2, 3, 4])
    with pytest.raises(ValueError):
        table.add_row(0, [1, 2, 3, 4])
    table.append_column("H", [5, 7, 10, 11, 12])
    with pytest.raises(ValueError):
        table.append_column("D", [6])
    table = Table([])
    table.append_column("D", [5, 7, 10])


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
    a = table.select_values(dict(a=datetime.date(2020, 3, 19)))
    assert a.nrows() == table.nrows() - 2
    a = table.select_values(dict(a=datetime.date(2020, 3, 19), b="Occitanie"))
    assert a.nrows() == 1


def test_select_columns():
    table1 = Table(["ID", "first_name"])
    table1.append_row([1, "Mark"])
    table1.append_row([2, "Steve"])
    table1.append_row([3, "James"])
    table1.append_row([4, "Tim"])
    table1.append_row([5, "Paul"])
    table1.append_row([6, "Clyde"])
    table = table1.select_columns(["first_name"])
    assert table.ncolumns() == 1
    assert table.nrows() == 6
    assert table.get_column("first_name") == table1.get_column("first_name")


def test_join():
    table1 = Table(["ID", "first_name"])
    table1.append_row([1, "Mark"])
    table1.append_row([2, "Steve"])
    table1.append_row([3, "James"])
    table1.append_row([4, "Tim"])
    table1.append_row([5, "Paul"])
    table1.append_row([6, "Clyde"])

    table2 = Table(["ID", "first_name"])
    table2.append_row([1, "Juan"])
    table2.append_row([2, "Tim"])
    table2.append_row([3, "Helmut"])
    table2.append_row([4, "Paul"])
    table2.append_row([5, "Steve"])
    table2.append_row([6, "Vicenzo"])

    table = table1.join(table2, "first_name")
    assert table.nrows() == 3
    assert table.ncolumns() == 3
    for ix in range(table.nrows()):
        row = table.get_row(ix)
        if ix == 0:
            assert row == [2, "Steve", 5]
        if ix == 1:
            assert row == [4, "Tim", 2]
        if ix == 2:
            assert row == [5, "Paul", 4]
