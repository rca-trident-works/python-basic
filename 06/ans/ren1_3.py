# whileループとcontinue文を使用して、1から100までの数字のうち、3で割り切れる数字だけを出力する

# continueを使用したバージョン
current_number = 1
while current_number <= 100:
    if current_number % 3 != 0:
        current_number += 1
        continue
    print(f"3で割り切れる数: {current_number}")
    current_number += 1

print()  # 空行を追加

# continue、セイウチ演算子を使用したバージョン
current_number = 0
while (current_number := current_number + 1) <= 100:
    if current_number % 3 != 0:
        continue
    print(f"3で割り切れる数: {current_number}")

print()  # 空行を追加

# continueを使用しないバージョン
current_number = 1
while current_number <= 100:
    if current_number % 3 == 0:
        print(f"3で割り切れる数: {current_number}")
    current_number += 1
