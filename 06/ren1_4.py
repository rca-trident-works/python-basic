# forループとbreak文を使用して、与えられたリストの要素が特定の条件を満たす場合にその要素とインデックスを出力し、
# 最初に条件を満たす要素が見つかったらループを終了する
# ・条件：リストの先頭と同じ値が存在している場合
# ・条件に合わない場合は、その旨を出力する

string = input("入力(,区切り): ")
array = string.split(",")
initial = array[0]

print('元のデータ: ' + str(array))
for i in range(len(array) - 1):
    if array[i + 1] == initial:
        print('最初の要素(' + initial + ')と同じ値が見つかりました')
        print('値: ' + str(array[i + 1]) + ', 位置: ' + str(i + 1 + 1) + '番目')
        break;

else:
    print('最初の要素と同じ値は見つかりませんでした')
