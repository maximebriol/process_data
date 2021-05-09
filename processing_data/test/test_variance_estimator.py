from ..table import Table
from ..variance_estimator import VarianceEstimator


def test_variance_estimator():
    table = Table(["A", "B", "C"])
    table.append_row([0, 4, 7])
    table.append_row([3, 5, 8])
    table.append_row([3, 6, 9])

    estimator = VarianceEstimator()
    other = estimator.fit(table)
    assert other.get_column("A") == [2]
