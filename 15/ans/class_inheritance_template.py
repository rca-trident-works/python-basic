class Shape:
    pass


class Triangle(Shape):
    pass


class Rectangle(Shape):
    pass


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
