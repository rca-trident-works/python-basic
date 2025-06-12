class SampleClass:
    def __init__(self, value):
        self.value = value
    def print_value(self):
        print(f"value: {self.value}")

obj2 = SampleClass(100)

print(type(obj2))
print(dir(obj2))
print(obj2.__dict__)

print('-' * 10)
print(obj2.value)
v = getattr(obj2, 'value')

print(v)
