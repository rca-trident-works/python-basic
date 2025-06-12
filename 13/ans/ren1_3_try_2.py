numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("インデックスを入力してください: "))
    print(f"リストの要素: {numbers[index]}")
except (ValueError, IndexError):
    print("無効なインデックスです")
