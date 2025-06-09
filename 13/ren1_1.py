value = input("数値を入力してください: ")

if value.isdigit():
    number = int(value)
    if number > 0:
        print("正の数整数です")
    else:
        print("負の値またはゼロが入力されました")
else:
    print("整数ではありません")
