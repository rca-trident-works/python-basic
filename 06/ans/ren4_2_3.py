data = [10, 1, 0, 30, 1, 20, 0, 5, 0, 60]

# この中から、目的の要素を全て削除する。
# [10, 1, 30, 1, 20, 5, 60] ← ほしい結果
ng_data = 0  # 不要なデータ

while ng_data in data:
    data.remove(ng_data)

print(data)
