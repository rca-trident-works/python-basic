from pprint import pprint


class Test:
    c_var = 10

    def func1(self):
        c_var = 30

    def func2(self):
        self.c_var = 40

    def func3(self):
        Test.c_var = 50


# 1
ins = Test()
pprint(ins.__dict__)
pprint(Test.__dict__)
print('-=' * 30)

# 2		以下 c_varのみ出力する
ins.c_var = 100
print(ins.__dict__['c_var'])
print(Test.__dict__['c_var'])

Test.c_var = 20
print(ins.__dict__['c_var'])
print(Test.__dict__['c_var'])
print('-=' * 30)

# 3
ins.func1()
print(ins.__dict__['c_var'])
print(Test.__dict__['c_var'])

ins.func2()
print(ins.__dict__['c_var'])
print(Test.__dict__['c_var'])

ins.func3()
print(ins.__dict__['c_var'])
print(Test.__dict__['c_var'])
