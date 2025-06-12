from typing import Union, List, Dict
DEFAULT_TAX_RATE = 10.0

def tax_include(price: int, tax_rate: float = DEFAULT_TAX_RATE) -> Union[int, None]:
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


def calc_tax(products_dict: Dict[str, List[int]]) -> Dict[str, List[int]]:
    """
    税込金額を計算し、リストに追加する
    全ての商品の消費税を計算し、結果を辞書にして返す
    """
    result_dict = {}
    for name, lst in products_dict.items():
        price, tax = lst
        tax_price = tax_include(price, tax)
        result_dict[name] = [price, tax, tax_price]
    return result_dict


# main
products = {
    "クッキー": [200, 8], 
    "少年ジャンプ": [264, 10], 
    "NotePC": [13400, 10]}

results = calc_tax(products)

for name, lst in results.items():
    price, tax, tax_price = lst
    print(f"商品名：{name},価格：{price},消費税：{tax},税込価格：{tax_price}")
