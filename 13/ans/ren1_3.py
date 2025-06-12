numbers = [10, 20, 30, 40, 50]
index = int(input("インデックスを入力してください: "))

if 0 <= index < len(numbers):
    print(f"リストの要素: {numbers[index]}")
else:
    print("インデックスが範囲外です")
