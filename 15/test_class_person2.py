import pytest
from class_person2 import Customer

@pytest.mark.parametrize(
    ("company_id", "company_name", "first_name", "last_name", "expected"),
    [
        (None, None, None, None, "名無しの権兵衛"),
        (1, None, "太郎", None, "名無しの太郎"),
        (2, "株式会社テスト", "太郎", "山田", "山田太郎"),
    ]
)
def test_full_name(company_id, company_name, first_name, last_name, expected):
    c = Customer(company_id, company_name, first_name, last_name)
    assert c.full_name == expected
    # なんの意味もないけど模範解答がこのテストをしてるので
    if company_id is not None:
        assert c.company_id == company_id
    if company_name is not None:
        assert c.company_name == company_name

# 模範解答通りのキーワード引数, インスタンス化後代入をテスト
@pytest.mark.parametrize(
    ("company_id", "company_name", "first_name", "last_name"),
    [
        (1, "株式会社テスト", "太郎", "山田"),
    ]
)
def test_keyword_args(company_id, company_name, first_name, last_name):
    c = Customer(company_id=company_id, 
                 company_name=company_name)
    c.first_name = first_name
    c.last_name = last_name
    assert c.full_name == "山田太郎"
    assert c.company_id == company_id
    assert c.company_name == company_name
