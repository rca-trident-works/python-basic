class Shape:
    member_count = 0
    def __init__(self):
        Shape.member_count += 1

    def area(self):
        pass

    def show_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def show_area(self):
        print(f"面積は{self.area():.1f}です")

class Rectangle(Shape):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def show_area(self):
        print(f"面積は{self.area()}です")
