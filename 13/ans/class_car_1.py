class Car:
    def __init__(self):
        self._maker = ''
        self._displacement = 0
        self._color = ''
        self._distance = 0
        self._turncount = 0

    @property
    def maker(self):
        return self._maker

    @maker.setter
    def maker(self, value):
        self._maker = value

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def run(self, km):
        """
        車を走らせる（バックしても走行距離に加える）
        Args:
            km (int): 走行距離（km）
        """
        print(f'{km}km走りました')
        self._distance += abs(km)

    def turn(self, direction):
        print(f'{direction}に曲がりました')
        self._turncount += 1

    def stop(self):
        """車を停止する"""
        print(f'止まりました。')

    def display(self):
        """車の情報を表示する"""
        print("【車種情報】")
        print(f"メーカー名:{self._maker}")
        print(f"排気量:{self._displacement}")
        print(f"色:{self._color}")
        print(f'全部で{self._distance}km走りました。')
        print(f'全部で{self._turncount}回曲がりました')


# main
car1 = Car()
car1.maker = 'HONDA'
car1.displacement = 2000
car1.color = 'Blue'
# print(car1.__dict__)

car2 = Car()
car2.maker = 'TOYOTA'
car2.displacement = 3000
car2.color = 'Red'
# print(car2.__dict__)

print("=== car1を走らせる ===")
car1.run(40)
car1.turn('右')
car1.run(30)
car1.turn('左')
car1.run(20)
car1.stop()

print("=== car2を走らせる ===")
car2.run(30)
car2.run(10)
car2.turn('右')
car2.turn('左')
car2.run(40)
car2.turn('右')
car2.stop()

print("=== 走行結果 ===")
car1.display()
car2.display()
