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

def resolve_key(val):
    for key, value in pref_jiscode.items():
        if val == value:
            return key
    return None

def validate(input_val):
    # check if input_val is number
    if input_val == "":
        return 1
    elif not input_val.isdigit():
        return 2
    elif int(input_val) < 1 or int(input_val) > 47:
        return 3
    else:
        return 0

def main():
    while True:
        input_val = input("都道府県コードを入力してください（1-47）: ")

        if validate(input_val) == 1:
            break
        elif validate(input_val) == 2:
            print("数字を入力してください")
            continue
        elif validate(input_val) == 3:
            print("1から47の範囲で入力してください")
            continue
        else:
            pref_name = resolve_key(int(input_val))
            print(f"都道府県コード {input_val} は {pref_name} です。")

if __name__ == "__main__":
    main()
