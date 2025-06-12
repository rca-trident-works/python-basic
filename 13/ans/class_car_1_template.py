class Car:
    pass


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
