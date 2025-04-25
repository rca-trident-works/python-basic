# 1から100までの数の中から、素数だけを出力する

for i in range(2, 101):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                print("素数:", i)
            else:
                break
