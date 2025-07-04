import re
import math

class Point:
    """2次元座標を管理する"""

    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    @property
    def position(self) -> tuple[float, float]:
        return (self._x, self._y)

    @position.setter
    def position(self, tuple_xy: tuple[float, float]):
        self._x, self._y = tuple_xy


def length(p1: Point, p2: Point) -> float:
    """2点間の距離・長さを求める"""
    p1_x, p1_y = p1.position
    p2_x, p2_y = p2.position
    distance_squared = (p1_x - p2_x) ** 2 + (p1_y - p2_y) ** 2
    return math.sqrt(distance_squared)


def triangle_area(a: float, b: float, c: float) -> float:
    """ヘロンの公式を用いて、面積を計算する"""
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def input_point() -> Point:
    """ユーザが座標の入力を行う"""
    while True:
        str_point = input("座標を入力してください x,y=").strip()
        m = re.match(r"^\s*(-?\d+(?:\.\d*)?)[\s,]*(-?\d+(?:\.\d*)?)\s*$", str_point)
        if not m:
            print("入力が正しい形式ではありません。再度入力してください。")
            continue
        try:
            float_x = float(m.group(1))
            float_y = float(m.group(2))
        except ValueError:
            print("数値として認識できません。再度入力してください。")
            continue
        print(f"入力された座標は ({float_x}, {float_y}) です。処理を続行します。")
        return Point(float_x, float_y)


if __name__ == "__main__":
    # 座標の入力
    p1 = input_point()
    p2 = input_point()
    p3 = input_point()

    # 三辺の計算
    length1 = length(p1, p2)
    length2 = length(p2, p3)
    length3 = length(p3, p1)

    # 面積の計算
    triangle = triangle_area(length1, length2, length3)
    print(f"三角形の面積={triangle}") 