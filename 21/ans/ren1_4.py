import math


def f(x):
    """計算に使用する関数の定義"""
    return 1.0 / x


def rectangular(start_x, end_x, n):
    """分割数nとして、矩形積分を行う"""
    # 1つの幅（分割後の幅）:h
    h = float((end_x - start_x)) / n
    s = 0

    for i in range(n):
        xi = start_x + i * h
        # 幅の中央 h/2.0
        rect = f(xi + h / 2.0) * h
        s += rect
    return s


def trapezoidal(start_x, end_x, n):
    """分割数nとして、台形積分を行う"""
    h = float((end_x - start_x)) / n
    s = 0

    for i in range(n):
        xi = start_x + i * h

        trap = 0.5 * (f(xi) + f(xi + h)) * h
        s += trap
    return s


def simpson(start_x, end_x, n):
    """分割数nとして、シンプソンの公式による積分を行う"""
    h = float((end_x - start_x)) / n
    s = f(start_x) + f(end_x)

    # シンプソンの公式: h/3 * [f(x0) + 4*f(x1) + f(x2)]
    for i in range(1, n):
        xi = start_x + i * h

        if i % 2 == 0:
            s += 2 * f(xi)
        else:
            s += 4 * f(xi)

    s *= h / 3
    return s


# 各アルゴリズムによる数値積分
n10 = 10
n10000 = 10000

print("** 矩形 **")
result = rectangular(2, 10, n10)
print(f"結果={result}\t分割数={n10}")
result = rectangular(2, 10, n10000)
print(f"結果={result}\t分割数={n10000}")
print("** 台形 **")
result = trapezoidal(2, 10, n10)
print(f"結果={result}\t分割数={n10}")
result = trapezoidal(2, 10, n10000)
print(f"結果={result}\t分割数={n10000}")
print("** Simpson **")
result = simpson(2, 10, n10)
print(f"結果={result}\t分割数={n10}")
result = simpson(2, 10, n10000)
print(f"結果={result}\t分割数={n10000}")

print("=" * 10)
print(f"真値={math.log(5)}")
