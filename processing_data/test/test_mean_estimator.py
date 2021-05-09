from ..table import Table
from ..mean_estimator import MeanEstimator


def test_mean_estimator():
    table = Table(["A", "B", "C", "D"])
    table.append_row([1, 1, 10, 100])
    table.append_row([1, 1, 10, 100])
    table.append_row([1, 1, 10, 100])
    table.append_row([2, 2, 20, 200])
    table.append_row([2, 2, 20, 200])
    table.append_row([2, 2, 20, 200])
    table.append_row([3, 3, 30, 300])
    table.append_row([3, 3, 30, 300])
    table.append_row([3, 3, 30, 300])
    table.append_row([4, 4, 40, 400])
    table.append_row([4, 4, 40, 400])
    table.append_row([4, 4, 40, 400])
    table.append_row([5, 5, 50, 500])
    table.append_row([5, 5, 50, 500])
    table.append_row([5, 5, 50, 500])

    estimator = MeanEstimator()
    other = estimator.fit(table)
    assert other.get_column("A") == [3]
    assert other.get_column("B") == [3]
    assert other.get_column("C") == [30]
    assert other.get_column("D") == [300]


