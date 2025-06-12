class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# main
x = MyClass()

print(MyClass.i)    # こっちで良い？
print(x.i)          # それとも？
print(x.f())
