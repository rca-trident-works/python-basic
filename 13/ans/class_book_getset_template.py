class Book:


















# main
b0 = Book(-100)  # 動作テスト用

b1 = Book(1000)
print(f'現在の値引率：{b1.get_discounts()}%')
b1.set_discounts(10)
print(f'現在の値引率：{b1.get_discounts()}%')
print(f'販売価格：{b1.price()}')

b2 = Book(2000)
print(f'現在の値引率：{b2.get_discounts()}%')
b2.set_discounts(-10)   # 動作テスト用
print(f'現在の値引率：{b2.get_discounts()}%')
print(f'販売価格：{b2.price()}')
