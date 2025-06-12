def func(a):
    """関数内関数のテスト"""
    def func_inner(b):
        print(b)
        return
    return func_inner(a)


# 一般的なmainの記述方法
if __name__ == "__main__":
    x = func(10)
    x = func(5)
