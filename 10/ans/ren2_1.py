# import math
from typing import Union # 型ヒントのUnion型を使用

def tax_include(price: int, tax_rate: float = 10.0) -> Union[int, None]:
# def tax_include(price: int, tax_rate: float = 10.0) -> int | None: # python3.10以降
# def tax_include(price, tax_rate = 10.0) # 型ヒントなしの場合
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
        # return math.floor(price * (1+tax_rate/100))


# main
price = 5000
# tax = 10 # デフォルト値を使用
print(f"{price}の税込金額は{tax_include(price)}円")

tax = 8
print(f"{price},消費税{tax}%の税込金額は{tax_include(price,tax)}円")

tax = -5
print(f"{price},消費税{tax}%の税込金額は{tax_include(price,tax)}円")
