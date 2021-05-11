import pytest
from ...table import Table
from ..cast import Cast


def test_normalisation():
    table = Table(["A", "B"])
    table.append_row(["0", ".0"])
    table.append_row(["1", ".1"])
    table.append_row(["2", ".2"])
    table.append_row(["3", ".3"])
    table.append_row(["4", ".4"])

    table = Cast(dict(A=int, B=float)).process(table)
    assert table.get_column("A") == [0, 1, 2, 3, 4]
    assert table.get_column("B") == [.0, .1, .2, .3, .4]
