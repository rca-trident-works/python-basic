import math


def taylor_sin(x, n):
    """sin(x)の近似値を求める"""
    x = math.radians(x)                     # 度→ラジアン 変換
    sin_approx = 0                          # approximate :近似値
    for i in range(0, n):
        coef = (-1) ** (i)                  # coefficients:係数
        num = x ** (2 * i + 1)              # numerator   :分子
        denom = math.factorial(2 * i + 1)   # denominator :分母
        sin_approx += (coef * num) / denom
    return sin_approx


angle = float(input("角度（度）を入力してください: "))
n = int(input("Taylor展開の次数を入力してください: "))

for i in range(1, n+1):
    approx_value = taylor_sin(angle, i)
    print(f"近似値({i}): {approx_value}")

true_value = math.sin(math.radians(angle))
error = abs(approx_value - true_value)

print(f"真値: {true_value}")
print(f"誤差: {error}")
