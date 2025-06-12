def check_shopping(order_dic) -> bool:
    ''' 辞書データのチェック
    すべてのデータが100円以上ならTrue
    1件でも100円未満であればFalse
    '''
    min_price = min(order_dic.values())
    if min_price < 100:
        return False
    else:
        return True


# main
order_dic = {}
while True:
    product_name = input('商品名を入力してください（0:終了）：')
    if product_name == '0':
        break

    product_price = input('金額を入力してください（0:終了）：')
    if product_price == '0':
        break
    elif product_price.isnumeric():
        price = int(product_price)
    else:
        print("数値以外が入力されました")
        continue

    order_dic[product_name] = price


if check_shopping(order_dic):
    print('\n全てのデータは問題ありませんでした')
else:
    print('\n最低価格を下回った商品があります。')

for key, value in order_dic.items():
    print(f'{key} : {value}')
