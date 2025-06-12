my_set = set("asdfghjkl")
print(my_set)

# 値の取り出し
for v in my_set:
    print(v)

# 添字と値の取り出し
for i, v in enumerate(my_set):
    print(i, "番目の要素は", v)

# 集合には内包表記が無いが同等の処理
new_set = set(v for v in my_set)
print(new_set)

# 要素の追加と削除
my_set.add('x')
my_set.remove('a')
print("要素追加・削除後:", my_set)

# 集合演算の例
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("和集合:", set1 | set2)
print("積集合:", set1 & set2)
print("差集合:", set1 - set2)

# 重複の除去
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print("重複を除去:", unique_numbers)

# 要素の存在確認
print("'a'は含まれているか:", 'a' in my_set)