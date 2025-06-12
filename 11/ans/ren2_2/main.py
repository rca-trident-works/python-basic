from math_operations import add, subtract, multiply, divide

a = float(input("最初の数値を入力してください: "))
b = float(input("2番目の数値を入力してください: "))

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")
