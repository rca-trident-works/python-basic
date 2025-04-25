# 1から100までの数の中から、素数だけを出力する

for i in range(2, 101):
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        print("素数:", i)
