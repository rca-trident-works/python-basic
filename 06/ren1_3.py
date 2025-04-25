# whileループとcontinue分を使用して、1から100までの数字のうち、3で割り切れる数字だけを出力する

count = 1
while count <= 100:
    count += 1
    if (count - 1) % 3 != 0:
        continue

    print (count - 1)
