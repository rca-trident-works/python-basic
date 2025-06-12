a = 1
print(f"a.id = {id(a)} {a=}")

a = 2
print(f"a.id = {id(a)} {a=}")

a = [1, 2, 3]
print(f"a.id = {id(a)} {a=}")
print(f"a[1].id = {id(a[1])} {a=}")

a[1] = 10
print(f"a.id = {id(a)} {a=}")
print(f"a[1].id = {id(a[1])} {a=}")

a = [4, 5]
print(f"a.id = {id(a)} {a=}")
