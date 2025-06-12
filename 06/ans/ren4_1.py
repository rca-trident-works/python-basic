fruits = ['バナナ', 'リンゴ', 'オレンジ']

while True:
    input_str = input("果物をカタカナで入力してください：")
    if input_str == '':
        break
    if input_str in fruits:
        print(f"{input_str}は、知っています！")
    else:
        print(f"{input_str}は、知りませんでした。覚えておきます。")
        fruits.append(input_str)

print('知っている果物')
print(fruits)
