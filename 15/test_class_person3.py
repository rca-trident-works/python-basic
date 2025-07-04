import pytest
from class_person3 import Person

@pytest.mark.parametrize(
    ("first_name", "last_name", "expected"),
    [
        (None, None, "氏名: 名無しの権兵衛"),
        ("太郎", None, "氏名: 名無しの太郎"),
        ("太郎", "山田", "氏名: 山田太郎"),
    ]
)
def test_show(capsys, first_name, last_name, expected):
    p = Person(first_name, last_name)
    p.show()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
