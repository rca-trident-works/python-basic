class SampleClass:
    def __init__(self, value) -> None:
        self.value = value

    def print_value(self) -> None:
        print(f'value : {self.value}')


obj2 = SampleClass(100)

print(type(obj2))
print(dir(obj2))
print(obj2.__dict__)

print('-'*10)
print(obj2.value)
v = getattr(obj2, 'value')
print(v)

print('-'*10)
obj2.print_value()
f0 = obj2.print_value
f0()

f1 = getattr(obj2, 'print_value')
f1()

f2 = getattr(obj2, 'print_value')()
f2
