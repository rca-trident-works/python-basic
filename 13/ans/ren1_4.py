num1 = int(input("第1の数値を入力してください: "))
num2 = int(input("第2の数値を入力してください: "))

if num2 != 0:
    result = num1 / num2
    print(f"結果: {result}")
else:
    print("ゼロで割り算はできません")
