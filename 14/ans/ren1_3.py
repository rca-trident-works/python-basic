class Car:
    def __init__(self, maker, model):
        self._maker = maker
        self._model = model

    def describe(self):
        print(f"自動車: {self._maker} - {self._model}")


class ElectricCar(Car):
    def __init__(self, maker, model, battery_size):
        super().__init__(maker, model)
        # size : kWh
        self._battery_size = battery_size

    def describe(self):
        print(
            f"電気自動車: {self._maker} - {self._model} (バッテリー容量：{self._battery_size}-kWh)")


# main
car = Car("Toyota", "Camry")
car.describe()

tesla = ElectricCar("Tesla", "Model S", 100)
tesla.describe()
