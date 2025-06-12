class ClassName:
    # クラス変数
    class_var = 0

    def __init__(self):
        # インスタンス変数の操作
        self.var = 1

    def func0(self, x):
        '''インスタンス変数へ追加'''
        self.var = self.var + x

    def func1(self):
        '''クラス変数へ追加'''
        # クラス変数の操作
        ClassName.class_var += 10        # できれば避けたい使い方(クラス名の変更時に問題有り)
        type(self).class_var += 100
        self.__class__.class_var += 1000


if __name__ == "__main__":
    obj = ClassName()
    print(obj.var)

    obj.var = 10
    print(obj.var)
    obj.func0(3)
    print(obj.var)

    print('-=' * 30)

    print(obj.class_var)
    obj.func1()
    print(obj.class_var)			# インスタンス変数class_varが存在しないので、クラス変数が参照される
    print(ClassName.class_var)
