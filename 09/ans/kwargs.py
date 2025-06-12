# argsとkwargsを併用する場合は、順番に注意
def say_dic(word, *args, **kwargs):
    print("word=", word)
    print("args=", args)
    print("kwargs", kwargs)
    for k, v in kwargs.items():
        print(k, v)
    print()


# 普通に呼び出す方法
say_dic('hello', 'Mike', 1, desert='banana', drink='beer')

# 辞書にしてから渡す方法
t = {'math': 15, 'science': 100}
say_dic('hi', 'Nancy', 2, **t)
