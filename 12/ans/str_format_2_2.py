def output(var):
    print(f'引数 = {var!r}')
    # print(f'引数 = {repr(var)}')


output('abc')
output('あいう\nかきく')
output(3.1415)

# eval() <- -> repr()

