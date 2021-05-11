from ...table import Table
from .. import Variance


def test_variance_estimator():
    table = Table(["A", "B", "C"])
    table.append_row([0, 4, 7])
    table.append_row([3, 5, 8])
    table.append_row([3, 6, 9])

    estimator = Variance()
    other = estimator.fit(table)
    assert other.get_column("A") == [2]
