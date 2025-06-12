# 必須引数と位置引数の組み合わせ
def print_more(required1, required2, *args):
    print("required1:", required1)
    print("required2:", required2)
    print("other:", args)


# 引数2個の場合
print_more(1, 2)
# required1: 1
# required2: 2
# other: ()

# 引数3個の場合
print_more(1, 2, 3)
# required1: 1
# required2: 2
# other: (3,)

# 引数5個の場合
print_more(1, 2, 3, 4, 5)
# required1: 1
# required2: 2
# other: (3, 4, 5)

# 必須引数が足りなければエラー
print_more(1)
# Traceback(most recent call last):
#     File "<stdin>", line 1, in <module >
#     print_more(1)
# TypeError: print_more() missing 1 required positional argument: 'required2'
