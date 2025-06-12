data = {"apple": 100, "banana": 200, "cherry": 300}
key = input("キーを入力してください: ")

if key in data:
    print(f"値: {data[key]}")
else:
    print("指定したキーは存在しません")
