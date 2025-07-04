# 計算結果の大きい方から足し込むと、情報落ちが発生する例
total_float = 0.0
for i in range(1, 100001):
    total_float += 1.0 / i
print("一般的な合計　：", total_float)


# 小さな値から足し込むことで、情報落ちを防ぐ
total_float = 0.0
for i in range(100000, 0, -1):
    total_float += 1.0 / i
print("より正確な合計：", total_float)


# 多倍長演算（任意精度10進演算）で、有効桁数を増やす
from decimal import Decimal, getcontext

# 情報落ちが発生した場合
getcontext().prec = 100
total_decimal = Decimal(0.0)
for i in range(1, 100001):
    total_decimal += Decimal(1.0) / Decimal(i)
print("一般的な合計　：", total_decimal)

# 情報落ちを抑制した場合
getcontext().prec = 100
total_decimal = Decimal(0.0)
for i in range(100000, 0, -1):
    total_decimal += Decimal(1.0) / Decimal(i)
print("より正確な合計：", total_decimal)
