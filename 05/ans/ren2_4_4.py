# 1から100までの数の中から、素数だけを出力する
#　エラトステネスの篩法

num_list = list(range(2,101))

for i in range(2, 101):
    if i in num_list:
        print("素数:", i)
        for j in range(i*2, 101, i):
            if j in num_list:
                num_list.remove(j)
