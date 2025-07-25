class Book:
    '''書籍の価格を管理するクラス'''
    _tax_rate = 0.1    # 10%

    def __init__(self, unit_price):
        if (unit_price < 0):
            raise ValueError("価格は0円以上で設定してください")
        self._unit_price = unit_price
        self._discount = 0

    def get_discounts(self):
        return self._discount

    def set_discounts(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("値引率は0-100で設定してください")

    def price(self):
        return int(self._unit_price * (1 - self._discount / 100)
                   * (1 + type(self)._tax_rate))


# main
# b0 = Book(-100)  # 動作テスト用

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
