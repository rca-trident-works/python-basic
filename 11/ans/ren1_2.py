import math

print("{0} {1:^10} {2:^10}".format("deg", "sin(x)", "cos(x)"))
for x in range(0, 91, 10):
    rad = math.radians(x)         # メソッドを使用した場合
    # rad = x * 2 * math.pi / 360 # 手計算の場合
    print(f'{x:2} {math.sin(rad):.8f} {math.cos(rad):.8f}')
