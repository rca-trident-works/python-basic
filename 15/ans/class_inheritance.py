class Shape:
    member_count = 0

    def __init__(self):
        Shape.member_count += 1

    def area(self):
        return 0

    def show_area(self):
        print(f'面積は{self.area()}です')


class Triangle(Shape):
    def __init__(self, base_length=1, height=1):
        super().__init__()
        self._base_length = base_length
        self._height = height

    def area(self):
        return self._base_length * self._height / 2


class Rectangle(Shape):
    def __init__(self, base_length=1, height=1):
        super().__init__()
        self._base_length = base_length
        self._height = height

    def area(self):
        return self._base_length * self._height


# Main:
print('Shapeを1個作成')
obj0 = Shape()
obj0.show_area()
print('Triangleを2個作成')
obj1 = Triangle()
obj2 = Triangle(10, 5)
obj1.show_area()
obj2.show_area()
print('Rectangleを2個作成')
obj3 = Rectangle()
obj4 = Rectangle(10, 5)
obj3.show_area()
obj4.show_area()
print(f'オブジェクトの個数：{Shape.member_count}')
