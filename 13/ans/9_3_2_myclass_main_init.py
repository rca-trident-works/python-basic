class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.ls = [1, 2, 3]

    def f(self):
        return 'hello world'


# main
x = MyClass()

print(x.i)
print(x.f())
print(x.ls)
