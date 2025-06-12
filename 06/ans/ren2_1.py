# 与えられたリストの各要素を2倍にして新しいリストを作成し出力

original_list = [1, 2, 3, 4, 5]

doubled_list = [x * 2 for x in original_list]
print(doubled_list)

# 内包表記を使用しない場合
doubled_list = []
for x in original_list:
    doubled_list.append(x * 2)
print(doubled_list)
