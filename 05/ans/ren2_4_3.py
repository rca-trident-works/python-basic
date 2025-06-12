# 1から100までの数の中から、素数だけを出力する

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(2, 101):
    if is_prime(i):
        print("素数:", i)
