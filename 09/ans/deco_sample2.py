def deco_nothing(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@deco_nothing
def test(n):
    for i in range(n):
        print(f'{i}回目のループです')

test(3)

