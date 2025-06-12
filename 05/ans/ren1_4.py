# 1以上100以下の偶数のみを掛算した結果を出力する

ans = 1
for num in range(2, 101, 2):
    ans *= num
print(ans)

ans = 1
for num in range(1, 101):
    if num % 2 == 0:
        ans *= num
print(ans)
