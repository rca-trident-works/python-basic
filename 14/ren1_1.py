class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def get_name(self):
        return self.name

class Dog(Animal):
    def speak(self):
        print(f"ワンワン!")

class Cat(Animal):
    def speak(self):
        print(f"ニャー")

# main
dog = Dog("スヌーピー")
cat = Cat("たま")

print(f'{dog.get_name()}: ', end='')
dog.speak()

print(f'{cat.get_name()}: ', end='')
cat.speak()
