var_global = 100


def func():
    # global var_global
    # var_global = 200
    print(var_global)
    var_local = 'A'
    # var_global = 'A'  # はどうなる？
    print(var_local)


print(var_global)
func()
print(var_global)
print(var_local)
