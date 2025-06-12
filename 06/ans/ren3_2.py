# 与えられた2次元リストの各要素を大文字に変換した2次元リストを作成

original_matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

uppercase_matrix = [[char.upper() for char in row] for row in original_matrix]
print(uppercase_matrix)
