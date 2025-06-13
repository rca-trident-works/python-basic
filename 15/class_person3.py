class Person:
    def __init__(self, first_name = None, last_name = None):
        if last_name is None:
            self.first_name = '権兵衛' if first_name is None else first_name
            self.last_name = '名無しの'
        else:
            self.first_name = first_name
            self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

    def show(self):
        return f"氏名: {self.full_name}"
