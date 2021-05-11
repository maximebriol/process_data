import pytest
from ..matrix import Matrix


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
