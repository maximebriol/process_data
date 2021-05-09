from ..normalisation_transformer import NormalisationTransformer
from .. table import Table

def test_normalisation():
    table=Table(["A","B"])
    table.append_row([0,0])
    table.append_row([1,1])

    norm = NormalisationTransformer()
    other = norm.transform(table)

    assert other.get_column("A") == [0,2]