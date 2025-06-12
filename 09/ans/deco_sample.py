def startend(func):
    '''startとendを前後に出力するデコレータ'''
    def funcname(*args, **kwargs):
        print('[start]--')
        reslut = func(*args, **kwargs)
        print('--[end]\n')
        return reslut
    return funcname


def test(n):
    print(f'test->{n}')


# main
test(10)    # 通常の呼出


# デコレータ使用
deco_func = startend(test)
deco_func(20)


# 同一の関数名でデコレータ使用(testを再定義)
test = startend(test)
test(30)


# @記法を使用する場合以下のように記述する
@startend
def test2(n):
    print(f'test2->{n}')


test2(100)
