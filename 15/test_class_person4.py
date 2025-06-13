import pytest
from class_person4 import Customer

@pytest.mark.parametrize(
    ("company_id", "company_name", "first_name", "last_name", "expected"),
    [
        (1, "株式会社テスト", "太郎", "山田", "氏名: 山田太郎\n\tid:1 会社名:株式会社テスト"),
    ]
)
def test_show(capsys, company_id, company_name, first_name, last_name, expected):
    c = Customer(company_id = company_id, 
                 company_name = company_name,
                 first_name = first_name,
                 last_name = last_name)
    c.show()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected

# 模範解答通りのキーワード引数, インスタンス化後代入をテスト
@pytest.mark.parametrize(
    ("company_id", "company_name", "first_name", "last_name", "expected"),
    [
        (1, "株式会社テスト", "太郎", "山田", "氏名: 山田太郎\n\tid:1 会社名:株式会社テスト"),
    ]
)
def test_keyword_args(capsys, company_id, company_name, first_name, last_name, expected):
    c = Customer(company_id=company_id, 
                 company_name=company_name)
    c.first_name = first_name
    c.last_name = last_name
    c.show()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
