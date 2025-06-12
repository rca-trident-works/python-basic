# 1から15までの奇数の積を計算して出力する

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for if
result = 1
for i in num:
    if i % 2 == 1:
        result *= i
print('for')
print('  奇数の積：', result)

# for range
result = 1
for i in range(1, 16, 2):
    result *= i
print('for_range')
print('  奇数の積：', result)
