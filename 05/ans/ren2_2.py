# 1から50までの偶数の合計を計算して出力する

num = range(0, 51, 2)

# sum
print('偶数の合計：', sum(num))

# for_range
total = 0
for i in num:
    total += i
print('偶数の合計：', total)

# for_range_if
total = 0
for i in range(51):
    if i % 2 == 0:
        total += i
print('偶数の合計：', total)
