# 与えられたリストから偶数のみを取り出して新しいリストを作成し出力

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in original_list if x % 2 == 0]
print(even_numbers)
