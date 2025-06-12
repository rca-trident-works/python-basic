def gen_pi4():
    lst = [1, 4, 1, 5]
    for i in lst:
        yield i


# main
for n in gen_pi4():
    print(n)
