from ..centrage_transformer import CentrageTransformer
from .. table import Table

def test_centrage():
    table=Table(["A","B","C"])
    table.append_row([1,2,3])
    table.append_row([4,5,6])
    table.append_row([7,8,9])

    centrage = CentrageTransformer()
    other = centrage.transform(table)

    assert other.get_column("A") == [-3,0,3]
