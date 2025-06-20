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

    # @property
    def full_name(self):
        return self._last_name + self._first_name
        # last_name,first_nameプロパティを利用する場合以下でもOK
        # return self.last_name + self.first_name

    # プロパティとして定義する場合
    # setterが不要な場合は記述しなくても良い
    # @property
    # def full_name(self):
    #     return self.first_name + self.last_name


# main
man = Person()
print(man.full_name())
# プロパティの場合
# print(man.full_name)

man = Person('花子')
print(man.full_name())
# プロパティの場合
# print(man.full_name)

man = Person('太郎', '山田')
print(man.full_name())
# プロパティの場合
# print(man.full_name)
