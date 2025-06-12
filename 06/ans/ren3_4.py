# 与えられた2次元リストの各要素の平均値を計算したリストを作成

original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

average_list = [sum(row) / len(row) for row in original_matrix]
print(average_list)
