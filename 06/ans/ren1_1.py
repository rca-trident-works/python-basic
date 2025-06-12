# whileとcontinueを使用して、1から10までの数字を出力する（3と7はスキップ）

# スキップする数字を定義
SKIP_NUMBERS = [3, 7]

# 方法1: 条件分岐の後にインクリメント
current_number = 1
while current_number <= 10:
    if current_number in SKIP_NUMBERS:
        current_number += 1
        continue
    print(f"数: {current_number}")
    current_number += 1

print()  # 区切り用の空行

# 方法2: ループの最初でインクリメント
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number in SKIP_NUMBERS:
        continue
    print(f"数: {current_number}")

print()  # 区切り用の空行
# 方法3: ループの最初でセイウチ演算子を利用（別の方法）
current_number = 0
while (current_number:=current_number + 1) <= 10:
    if current_number in SKIP_NUMBERS:
        continue
    print(f"数: {current_number}")

