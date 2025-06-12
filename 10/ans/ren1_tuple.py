tpl = (1, 2, 3, 4, 5, 6)
print(tpl)

# for での取り出し
for n in tpl:
    print(n)

# 添字と値の取り出し
for i, n in enumerate(tpl):
    print(i, "番目の要素は", n)

# タプルには内包表記は無いが同等の処理
new_tpl = tuple(n for n in tpl)
print(new_tpl)

# スライシングの例
print(tpl[1:4])  # 2番目から4番目までの要素を取得

# アンパックの例
a, b, c, d, e, f = tpl
print(f"アンパック結果: {a}, {b}, {c}")
