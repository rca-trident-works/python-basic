import random
pref_jiscode = {
    "北海道": 1,
    "青森県": 2,
    "岩手県": 3,
    "宮城県": 4,
    "秋田県": 5,
    "山形県": 6,
    "福島県": 7,
    "茨城県": 8,
    "栃木県": 9,
    "群馬県": 10,
    "埼玉県": 11,
    "千葉県": 12,
    "東京都": 13,
    "神奈川県": 14,
    "新潟県": 15,
    "富山県": 16,
    "石川県": 17,
    "福井県": 18,
    "山梨県": 19,
    "長野県": 20,
    "岐阜県": 21,
    "静岡県": 22,
    "愛知県": 23,
    "三重県": 24,
    "滋賀県": 25,
    "京都府": 26,
    "大阪府": 27,
    "兵庫県": 28,
    "奈良県": 29,
    "和歌山県": 30,
    "鳥取県": 31,
    "島根県": 32,
    "岡山県": 33,
    "広島県": 34,
    "山口県": 35,
    "徳島県": 36,
    "香川県": 37,
    "愛媛県": 38,
    "高知県": 39,
    "福岡県": 40,
    "佐賀県": 41,
    "長崎県": 42,
    "熊本県": 43,
    "大分県": 44,
    "宮崎県": 45,
    "鹿児島県": 46,
    "沖縄県": 47
}

# 逆引きを作成
jiscode_pref = {v: k for k, v in pref_jiscode.items()}
# jiscode_pref = {}
# for k, v in pref_jiscode.items():
#     jiscode_pref[v] = k

random_code = random.randrange(1, 47+1)
input_count = 0


print(f'{jiscode_pref[random_code]}の県コードを当ててください')
while True:
    pref_code = input('県コードを入力してください：')
    # 空改行の場合は終了する
    if pref_code == '':
        break

    # 入力値が数字でない場合の処理
    try:
        pref_code_int = int(pref_code)
    except ValueError:
        print("数値を入力してください。")
        continue

    # 入力値の範囲チェック
    if pref_code_int < 1 or pref_code_int > 47:
        continue

    input_count += 1
    if random_code == pref_code_int:
        print('正解!')
        print(f'都道府県名：{jiscode_pref[pref_code_int]}　県コード：{pref_code_int}')
        print(f'{input_count}回で正解しました！')
        break
    elif pref_code_int < random_code:
        print('入力した値は小さいです')
    elif pref_code_int > random_code:
        print('入力した値は大きいです')
    print()
