class Flyable:
    def fly(self):
        print("空を飛べる!")

class Swimmable:
    def swim(self):
        print("水中を泳げる!")

class FlyingFish(Flyable, Swimmable):
    def perform_actions(self):
        self.fly()
        self.swim()

# main
fish = FlyingFish()
fish.perform_actions()
