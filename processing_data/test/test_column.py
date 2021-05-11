import pytest
from ..column import Columns


def test_columns():
    columns = ["A", "B", "C"]
    obj = Columns(columns)

    assert obj.columns() == columns
    assert id(obj.columns()) != id(columns)
    assert obj.get_index("B") == 1
    assert obj.get_name(1) == "B"
    assert obj.get_length() == 3

    obj.remove("A")
    assert obj.get_index("B") == 0
    assert obj.get_name(0) == "B"
    assert obj.get_length() == 2

    obj.append("A")
    assert obj.get_length() == 3
    assert obj.get_index("A") == 2
    assert obj.get_name(2) == "A"

    with pytest.raises(ValueError):
        obj.append("A")

    obj.insert("D", 2)
    assert obj.get_length() == 4
    assert obj.get_index("A") == 3
    assert obj.get_index("D") == 2
    assert obj.get_name(2) == "D"

    with pytest.raises(ValueError):
        obj.insert("X", -1)

    with pytest.raises(ValueError):
        obj.insert("X", 4)