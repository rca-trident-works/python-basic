class HumanBase:
    def __init__(self, name) -> None:
        self.name = name

    def say_name(self) -> None:
        print(f'私の名前は「{self.name}」です。')

# main
h1 = HumanBase('吉村')
h2 = HumanBase('佐藤')

h1.say_name()
h2.say_name()
