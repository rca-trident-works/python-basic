num = 100
ans = ""
while num > 0:
    mod = num % 2
    ans += str(mod)
    num = int(num/2)  # num = num // 2
print(ans[::-1])

# 反転しておく
ans = ans[::-1]
print(ans)

# 別解
num = 100
ans = ""
while num > 0:
    mod = num % 2
    ans = str(mod) + ans
    num = int(num/2)
print(ans)
