def sample(a, b, c):
    print(f'a => {a}')
    print(f'b => {b}')
    print(f'c => {c}')
    print("-="*10)


# 混在での呼び出し
sample(10, c=20, b=30)  # OK

sample(10, 20, c=30)  # OK

sample(10, a=20, b=30)  # NG

sample(a=20, b=30, 40)  # NG
