# 要素が偶数なら"Even"、奇数なら"Odd"という文字列に変換し出力

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)
