import pytest
from ..normalisation_transformer import NormalizationTransformer
from ..table import Table


def test_normalisation():
    table = Table(["A", "B"])
    table.append_row([0, 0])
    table.append_row([1, 10])
    table.append_row([2, 20])
    table.append_row([3, 30])
    table.append_row([4, 40])

    norm = NormalizationTransformer()
    other = norm.transform(table)

    assert [-1.41421356, -0.70710678, 0., 0.70710678,
            1.41421356] == pytest.approx(other.get_column("A"))
    assert [-1.41421356, -0.70710678, 0., 0.70710678,
            1.41421356] == pytest.approx(other.get_column("B"))
