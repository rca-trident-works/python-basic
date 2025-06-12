# forとbreakを使用して、入力された文字列が回文かどうかを判定する。

# 1文字ずつチェック
input_string = input('回文かどうかを判定する文字列を入力してください：')

for i in range(len(input_string) // 2):
    if input_string[i] != input_string[-(i + 1)]:
        print('回文ではない')
        break
else:
    print('回文です')

print()  # 空行を追加

# 別バージョン
# 文字列を反転させてチェック
reversed_string = input_string[::-1]
for i in range(len(input_string)//2):
    if input_string[i] != reversed_string[i]:
        print('回文ではない')
        break
else:
    print('回文です')
