import pytest
from ..table import Table


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


def test_str():
    table = Table(["jour", "nomReg", "numReg", "incid_rea"])

    table.append_row(["2020-03-19", "Auvergne-Rhone-Alpes", 84, 44])
    table.append_row(["2020-03-19", "Bourgogne-Franche-Comte", 27, 33])
    table.append_row(["2020-03-19", "Bretagne", 53, 8])
    table.append_row(["2020-03-19", "Centre-Val de Loire", 24, 6])
    table.append_row(["2020-03-19", "Corse", 94, 11])
    table.append_row(["2020-03-19", "Grand-Est", 44, 69])
    table.append_row(["2020-03-19", "Guadeloupe", 1, 0])
    table.append_row(["2020-03-19", "Guyane", 3, 0])
    table.append_row(["2020-03-19", "Hauts-de-France", 32, 37])
    table.append_row(["2020-03-19", "Ile-de-France", 11, 151])
    table.append_row(["2020-03-19", "La Réunion", 4, 0])
    table.append_row(["2020-03-19", "Martinique", 2, 0])
    table.append_row(["2020-03-19", "Mayotte", 6, 0])
    table.append_row(["2020-03-19", "Normandie", 28, 7])
    table.append_row(["2020-03-19", "Nouvelle-Aquitaine", 75, 7])
    table.append_row(["2020-03-19", "Occitanie", 76, 29])
    table.append_row(["2020-03-19", "Pays de la Loire", 52, 11])
    table.append_row(["2020-03-19", "Provence-Alpes-Cote d'Azur", 93, 25])
    table.append_row(["2020-03-20", "Auvergne-Rhone-Alpes", 84, 16])
    table.append_row(["2020-03-20", "Bourgogne-Franche-Comte", 27, 9])
    table.append_row(["2020-03-20", "Bretagne", 53, 2])

    assert str(
        table
    ) == """          jour                      nomReg  numReg  incid_rea
0   2020-03-19        Auvergne-Rhone-Alpes      84         44
1   2020-03-19     Bourgogne-Franche-Comte      27         33
2   2020-03-19                    Bretagne      53          8
3   2020-03-19         Centre-Val de Loire      24          6
4   2020-03-19                       Corse      94         11
5   2020-03-19                   Grand-Est      44         69
6   2020-03-19                  Guadeloupe       1          0
7   2020-03-19                      Guyane       3          0
8   2020-03-19             Hauts-de-France      32         37
9   2020-03-19               Ile-de-France      11        151
10  2020-03-19                  La Réunion       4          0
11  2020-03-19                  Martinique       2          0
12  2020-03-19                     Mayotte       6          0
13  2020-03-19                   Normandie      28          7
14  2020-03-19          Nouvelle-Aquitaine      75          7
15  2020-03-19                   Occitanie      76         29
16  2020-03-19            Pays de la Loire      52         11
17  2020-03-19  Provence-Alpes-Cote d'Azur      93         25
18  2020-03-20        Auvergne-Rhone-Alpes      84         16
19  2020-03-20     Bourgogne-Franche-Comte      27          9
20  2020-03-20                    Bretagne      53          2"""

    assert table.to_csv() == """jour;nomReg;numReg;incid_rea
2020-03-19;Auvergne-Rhone-Alpes;84;44
2020-03-19;Bourgogne-Franche-Comte;27;33
2020-03-19;Bretagne;53;8
2020-03-19;Centre-Val de Loire;24;6
2020-03-19;Corse;94;11
2020-03-19;Grand-Est;44;69
2020-03-19;Guadeloupe;1;0
2020-03-19;Guyane;3;0
2020-03-19;Hauts-de-France;32;37
2020-03-19;Ile-de-France;11;151
2020-03-19;La Réunion;4;0
2020-03-19;Martinique;2;0
2020-03-19;Mayotte;6;0
2020-03-19;Normandie;28;7
2020-03-19;Nouvelle-Aquitaine;75;7
2020-03-19;Occitanie;76;29
2020-03-19;Pays de la Loire;52;11
2020-03-19;Provence-Alpes-Cote d'Azur;93;25
2020-03-20;Auvergne-Rhone-Alpes;84;16
2020-03-20;Bourgogne-Franche-Comte;27;9
2020-03-20;Bretagne;53;2"""