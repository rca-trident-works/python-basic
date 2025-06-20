class Person:
    def __init__(self, first_name='権兵衛', last_name='名無しの'):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def full_name(self):
        return self.last_name + self.first_name

    def show(self):
        print(f'氏名：{self.full_name}')


class Customer(Person):
    def __init__(self, first_name='権兵衛', last_name='名無しの', company_id=0, company_name=''):
        super().__init__(last_name, first_name)
        self.company_id = company_id
        self.company_name = company_name

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, id):
        self._company_id = id

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, name):
        self._company_name = name


# main
man = Person('太郎', '山田')
man.show()

cust = Customer(company_id=10, company_name='橋本商会')
cust.first_name = '花子'
cust.last_name = '鈴木'
cust.show()
