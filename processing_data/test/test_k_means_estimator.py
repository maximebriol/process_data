import pytest
from ..k_means_estimator import euclidean_distance, center_class, KMeansEstimator
from ..table import Table


def test_euclidean_distance():
    assert 2.23606797749979 == pytest.approx(euclidean_distance([1, 2],
                                                                [2, 0]))


def test_center_class():
    assert center_class([[1, 2], [2, 5]]) == [1.5, 3.5]


def test_k_means():
    table = Table(["A", "B", "C", "D"])
    table.append_row([100, 2, 2, 1])
    table.append_row([100, 2, 4, 0])
    table.append_row([100, 2, 1, 1])
    KMeansEstimator().k_means(2, table)


