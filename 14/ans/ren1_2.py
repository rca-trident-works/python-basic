class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("ガサゴソッ")


class Lion(Animal):
    def make_sound(self):
        super().make_sound()
        print("ガオォーー！")


# main
tiger = Animal("Tiger")
tiger.make_sound()

lion = Lion("Lion")
lion.make_sound()
