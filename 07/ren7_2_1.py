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

def validate(input_val):
    if input_val == "":
        return 1
    # 都道府県で終わっているか
    elif input_val[-1] != "都" and input_val[-1] != "道" and input_val[-1] != "府" and input_val[-1] != "県":
        return 2
    else:
        return 0

def main():
    while True:
        input_val = input("都道府県を入力してください: ")

        result = validate(input_val)
        if result == 1:
            break
        elif result == 2:
            print("都道府県まで入力してください")
            continue
        else:
            # 都道府県の番号を取得
            pref_code = pref_jiscode.get(input_val)
            if pref_code is not None:
                print(f"{input_val}の番号は{pref_code}")
            else:
                print(f"{input_val}県の県コードは見つかりませんでした")


if __name__ == "__main__":
    main()
