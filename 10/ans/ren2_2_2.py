from typing import Union, List, Dict
DEFAULT_TAX_RATE = 10.0


def tax_included(price: int, tax_rate: float = DEFAULT_TAX_RATE) -> Union[int, None]:
    """税込金額を計算する関数

    Args:
        price (int): 税抜き金額
        tax_rate (float, optional): 税率（%）。デフォルトは10.0

    Returns:
        Union[int, None]: 税込金額（小数点以下切り捨て）。不正な税率の場合はNone
    """

    if tax_rate < 0:
        return None
    else:
        return int(price * (1 + tax_rate / 100))


def calc_tax(products_dict : Dict[str, List[int]]) -> None:
    """
    消費税を計算し、リストに直接追加する
    """
    for _, lst in products_dict.items():
        price, tax = lst
        lst.append(tax_included(price, tax))


# main
products = {
    "クッキー": [200, 8], 
    "少年ジャンプ": [264, 10], 
    "NotePC": [13400, 10]}

calc_tax(products)

for name, lst in products.items():
    price, tax, tax_price = lst
    print(f"商品名：{name},価格：{price},消費税：{tax},税込価格：{tax_price}")
