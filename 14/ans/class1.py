class TestClass:
    pass


obj1 = TestClass()

print(type(obj1))       # 型を出力
print(dir(obj1))        # 全ての変数・メソッド等を出力
print(obj1.__dict__)    # 属性と値を出力
