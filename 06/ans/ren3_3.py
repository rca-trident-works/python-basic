# 与えられた2次元リストの各要素を絶対値に変換した2次元リストを作成

original_matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]

absolute_matrix = [[abs(x) for x in row] for row in original_matrix]
print(absolute_matrix)
