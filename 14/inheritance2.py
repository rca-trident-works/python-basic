class HumanBase:
    def __init__(self, name) -> None:
        self.name = name

    def say_name(self) -> None:
        print(f'私の名前は「{self.name}」です。')

class Human(HumanBase):
    def __init__(self, name, birthday) -> None:
        super().__init__(name)
        self.birthday = birthday

    def say_birthday(self) -> None:
        print(f'誕生日は{self.birthday}です。')

# main
h1 = Human('吉村', '2000-01-01')
h2 = Human('佐藤', '2010-12-31')

h1.say_name()
h1.say_birthday()

h2.say_name()
h2.say_birthday()
