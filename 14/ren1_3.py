class Car:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def describe(self):
        pass

class ElectricCar(Car):
    def __init__(self, maker, model, battery_size):
        super().__init__(maker, model)
        self.battery_size = battery_size
    def describe(self):
        print(f"電気自動車: {self.maker} - {self.model} (バッテリー容量: {self.battery_size}-kWh)")

# main
tesla = ElectricCar("Tesla", "Model S", 100)
tesla.describe()
