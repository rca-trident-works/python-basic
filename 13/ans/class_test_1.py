from pprint import pprint


class Test:
    c_var = 10


# 1
ins = Test()
print(ins.c_var)
print(ins.__dict__)
pprint(Test.__dict__)
