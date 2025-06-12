x = 10
# while (x=x-1) > 0:    # Errorになる
while (x:=x-1) > 0:
    print(x)

# 別解
x = 10
while x > 1:
    x -= 1
    print(x)

# 別解
x = 9
while x > 0:
    print(x)
    x -= 1

