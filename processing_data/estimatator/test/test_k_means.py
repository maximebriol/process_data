import pytest
from ...table import Table
from ..k_means import euclidean_distance, center_class, KMeans


def test_euclidean_distance():
    assert pytest.approx(euclidean_distance([1, 2],
                                            [2, 0])) == 2.23606797749979


def test_center_class():
    assert center_class([[1, 2], [2, 5]]) == [1.5, 3.5]


def test_k_means():
    table = Table(["A", "B", "C", "D"])
    table.append_row([100, 2, 2, 1])
    table.append_row([100, 2, 4, 0])
    table.append_row([100, 2, 1, 1])
    KMeans().calculate(2, table)

    table = Table(["A", "B", "C"])
    table.append_row([100, 100, 100])
    table.append_row([2, 2, 2])
    table.append_row([2, 4, 1])
    table.append_row([1, 0, 1])
    KMeans().calculate(2, table)
