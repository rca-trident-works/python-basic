# 与えられた2次元リストの各要素を2倍にした2次元リストを作成

original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

doubled_matrix = [[x * 2 for x in row] for row in original_matrix]
print(doubled_matrix)

# 別解
doubled_matrix_map = [list(map(lambda x: x * 2, row)) for row in original_matrix]
print(doubled_matrix_map)

# ループを使用した別解
doubled_matrix_loop = []
for row in original_matrix:
    doubled_row = []
    for x in row:
        doubled_row.append(x * 2)
    doubled_matrix_loop.append(doubled_row)
print(doubled_matrix_loop)
