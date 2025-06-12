numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("インデックスを入力してください: "))
    print(f"リストの要素: {numbers[index]}")
except ValueError:
    print("無効なインデックスです")
except IndexError:
    print("インデックスがリストの範囲を超えています")
