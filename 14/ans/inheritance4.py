class HumanBase:
    def __init__(self, name) -> None:
        self.name = name

    def say_name(self) -> None:
        print(f'私の名前は「{self.name}」です')


class Human(HumanBase):
    def __init__(self, name, birthday) -> None:
        super().__init__(name)
        self.birthday = birthday

    def say_birthday(self) -> None:
        print(f'誕生日は{self.birthday}です')


class Woman(Human):
    def __init__(self, name, birthday) -> None:
        super().__init__(name, birthday)
        self.sex = '女'


class Man(Human):
    def __init__(self, name, birthday) -> None:
        super().__init__(name, birthday)
        self.sex = '男'


# main
h1 = Woman('吉村', '2000-01-01')
h2 = Man('佐藤', '2010-12-31')


def func():
    print('性別は女です')

# インスタンスh1に関数say_sexを追加
setattr(h1, 'say_sex', func)

h1.say_name()
h1.say_birthday()
h1.say_sex()        # h1は問題なく動作
h2.say_name()
h2.say_birthday()
h2.say_sex()        # h2には関数がないのでError
