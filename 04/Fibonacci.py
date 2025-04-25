# フィボナッチ級数
# 2項の和により次項が定まる
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
