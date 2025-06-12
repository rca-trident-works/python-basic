data = {"apple": 100, "banana": 200, "cherry": 300}
key = input("キーを入力してください: ")

try:
    print(f"値: {data[key]}")
except KeyError:
    print("指定したキーは存在しません")
