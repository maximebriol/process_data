from ..aggregation import Aggregation
from ..table import Table


def test_agg():
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

    agg = Aggregation(["A", "B"])
    mean = agg.transform(table)
    assert mean.ncolumns() == 4
    assert mean.nrows() == 5

    for ix in range(mean.nrows()):
        row = mean.get_row(ix)
        ix += 1
        assert row == [ix, ix, ix * 10, ix * 100]
