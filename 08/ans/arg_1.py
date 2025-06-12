def sample(a, b, c):
    print(f'a => {a}')
    print(f'b => {b}')
    print(f'c => {c}')
    print("-="*10)


# 通常の呼び出し（位置引数）
sample(10, "abc", 20)

sample("xyz", "123", 45)

# キーワード引数での呼び出し
sample(a=10, c="abc", b=20)

sample(c=10, a="abc", b=20)
