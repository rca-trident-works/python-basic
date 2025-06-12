try:
    value = int(input("数値を入力してください: "))
    if value > 0:
        print("正の整数です")
    else:
        print("負の値またはゼロが入力されました")
except ValueError:
    print("整数を入力してください")
