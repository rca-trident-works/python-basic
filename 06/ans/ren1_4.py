# リスト内で最初の要素と同じ値を持つ要素を探し、
# その要素とインデックスを出力するプログラム

numbers = [3, 7, 1, 5, 7, 3, 9, 1]
# numbers = [3, 7, 1, 5, 7, 9, 1]   # 別のデータで検証

print('元のデータ：', numbers)

first_element = numbers[0]

for index, value in enumerate(numbers):
    if index == 0:
        continue  # 最初の要素は自分自身なのでスキップ
    if value == first_element:
        print(f"最初の要素({first_element})と同じ値が見つかりました")
        print(f"値: {value}, 位置: {index}番目")
        break
else:
    print('最初の要素と同じ値は見つかりませんでした')
