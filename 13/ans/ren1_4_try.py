try:
    num1 = int(input("第1の数値を入力してください: "))
    num2 = int(input("第2の数値を入力してください: "))
    result = num1 / num2
    print(f"結果: {result}")
except ValueError:
    print("整数を入力してください")
except ZeroDivisionError:
    print("ゼロで割り算はできません")
