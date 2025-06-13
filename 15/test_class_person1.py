import pytest
from class_person1 import Person

@pytest.mark.parametrize(
    ("first_name", "last_name", "expected"),
    [
        (None, None, "名無しの権兵衛"),
        ("太郎", None, "名無しの太郎"),
        ("太郎", "山田", "山田太郎"),
    ]
)
def test_full_name(first_name, last_name, expected):
    p = Person(first_name, last_name)
    assert p.full_name == expected
