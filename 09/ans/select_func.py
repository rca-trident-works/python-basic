# 関数を辞書で管理し、実行する
def func1():
    print("Hello\n")


def func2():
    print("Goodbye\n")


def func3():
    print("Hehehe\n")


# 一般的なmainの記述方法
if __name__ == "__main__":
    run_list = {'a': func1, 'b': func2, 'c': func3}

    while True:
        for k, v in run_list.items():
            print(f"{k}=>{v.__name__} ", end='')
        print()

        select = input('どちらを実行しますか？:')

        if select == '':
            break
        if select in run_list.keys():
            run_list[select]()
        else:
            print('どちらかを選択してください。')
