class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        '''鳴き声を出すメソッド
            各クラスで実装すること
        '''
        pass


class Dog(Animal):
    def speak(self):
        print("ワンワン！")


class Cat(Animal):
    def speak(self):
        print("ニャー")


# main
dog = Dog("スヌーピー")
cat = Cat("たま")

print(f'{dog.get_name()}:', end='')
dog.speak()
print(f'{cat.get_name()}:', end='')
cat.speak()
