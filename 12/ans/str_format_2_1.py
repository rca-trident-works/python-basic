def output(var):
    if isinstance(var, str):
        if '\n' in var:
            var = var.replace('\n', '\\n')
        print(f"引数 = '{var}'")
    else:
        print(f"引数 = {var}")


def output2(var):
    if isinstance(var, str):
        print(f"引数 = '", end='')
        for ch in var:
            if ch == '\n':
                ch = '\\n'
            print(ch, end='')
        print("'")
    else:
        print(f"引数 = {var}")


output('abc')
output('あいう\nかきく')
output(3.1415)
output2('abc')
output2('あいう\nかきく')
output2(3.1415)
