from pprint import pprint


class Test:
    c_var = 10


# 1
ins = Test()
pprint(ins.__dict__)
pprint(Test.__dict__)
print('-=' * 30)

# 2
ins.c_var = 100
pprint(ins.__dict__)
pprint(Test.__dict__)

Test.c_var = 20
pprint(ins.__dict__)
pprint(Test.__dict__)
