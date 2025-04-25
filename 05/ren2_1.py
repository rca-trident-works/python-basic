# 1から10までの整数の合計を計算して出力する

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# forで合計を求める
total = 0
for i in num:
    total += i
print('for')
print('  合計 :', total)

# forでrange()を使用
total = 0
for i in range(11):
    total += i
print('for_range')
print('  合計 :', total)

# whileで合計を求める
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print('while')
print('  合計 :', total)

# 関数sum()を使用
print('sum')
print('  合計 :', sum(num))

# sum() と range() を使用
print('sum_range')
print('  合計 :', sum(range(11)))

# printのみ
print('printのみ')
print('  合計 :', 1+2+3+4+5+6+7+8+9+10)
