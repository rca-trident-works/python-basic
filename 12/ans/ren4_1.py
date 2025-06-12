DATA_FILENAME = 'test.csv'


def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    if isinstance(s, str):
        if s.isnumeric():
            return int(s)
        else:
            return 0
    else:
        return s


def list2int(s):
    """list2int 文字列を数値に変換した値を返す（List対応）"""
    if isinstance(s, str):
        return str2int(s)
    elif isinstance(s, list):
        result = [str2int(i) for i in s]
        return result
    else:
        return None


# ファイルの読み込み
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []                                    # 1人分のデータを入れるリスト
    title = f.readline()                                # 1行目の読み込み
    for line in f:                                      # 残りの行を読み込み
        line = line.strip()                             # 行末の改行を取り除く
        person_data.append(line.split(','))             # 「,」で分割して格納
        # person_data.append(line.strip().split(','))   # まとめて書いてもOK


# 一人分ずつ合計を求める
for data in person_data:                                # 各人のデータを1人分ずつ処理
    name, scores_str = data[0], data[1:]                # 名前と得点に分ける
    # scores = [int(num) for num in scores_str]         # 文字列を数字に変換 内包表記を使用
    scores = list2int(scores_str)                       # 文字列を数字に変換 過去に作った関数を使用
    total = sum(scores)                                 # 合計を求める
    print(name, total)                                  # 一人分ずつ出力
