import os

DATA_FILENAME = 'word.txt'

# ファイルが存在する場合、単語リストを読み込む
#  try - exceptを使用する方が良い
if os.path.isfile(DATA_FILENAME):
    # ファイルから単語リストを読み込む
    with open(DATA_FILENAME, 'r', encoding='utf8') as f:
        words_list = [word.strip() for word in f]
else:
    words_list = []

while True:
    input_word = input('単語を入力してください：')
    if input_word == "":
        break
    if input_word == 'LIST':
        print('単語リスト：', words_list)
        continue
    if input_word in words_list:
        print('すでに登録済です')
        continue
    else:
        words_list.append(input_word)

# 終了時のメッセージ
print('終了します')
print('これまでに覚えた単語：', words_list)

# ファイルに単語リストを書き込む
with open(DATA_FILENAME, 'w', encoding='utf8') as f:
    for word in words_list:
        f.write(f'{word}\n')
