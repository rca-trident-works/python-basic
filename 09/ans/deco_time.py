import time


def run_time(func):
    '''実行時間を計測・出力するデコレータ'''
    def funcname(*args, **kwargs):
        starttime = time.time()
        result = func(*args, **kwargs)
        print(f'実行関数:{func.__name__} 実行時間：{time.time()-starttime}')
        # 小数点以下3桁まで表示する場合
        # print(f'実行関数:{func.__name__} 実行時間：{time.time()-starttime:.3f}')
        return result
    return funcname

# main

@run_time
def test(n):
    for i in range(n):
        time.sleep(i)   # i秒ウェイトする


test(3)
test(5)
