class Book:




















#main
b1 = Book(1000)
print(f'現在の値引率：{b1.discounts}%')
b1.discounts = 10
print(f'現在の値引率：{b1.discounts}%')
print(f'販売価格：{b1.price()}')

b2 = Book(2000)
print(f'現在の値引率：{b1.discounts}%')
b1.discounts = -10
print(f'現在の値引率：{b1.discounts}%')
print(f'販売価格：{b1.price()}')
