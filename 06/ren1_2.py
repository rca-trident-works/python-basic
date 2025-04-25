# forとbreakを使用して, 入力された文字列が回文（前から読んでも後ろから読んでも同じ）かどうかを判定する

input_string = input("文字列を入力してください: ")

for i in range(len(input_string) // 2):
    if input_string[i] != input_string[-(i + 1)]:
        print("回文ではありません")
        break

    if i == len(input_string) // 2 - 1:
        print("回文です")
        break
