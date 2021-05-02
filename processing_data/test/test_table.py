import pytest
from ..table import Columns, Table, Matrix


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
