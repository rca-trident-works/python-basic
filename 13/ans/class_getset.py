class TestGetSet:
    def __init__(self, val):
        self.__val = val

    def get_val(self):
        return self.__val

    def set_val(self, val):
        self.__val = val


class TestProperty:
    def __init__(self, val):
        self.__val = val

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val


# main
obj1 = TestGetSet(100)
print(obj1.get_val())
obj1.set_val(20)
print(obj1.get_val())

obj2 = TestProperty(100)
print(obj2.val)
obj2.val = 20
print(obj2.val)
