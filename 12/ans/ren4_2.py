DATA_FILENAME = 'test.csv'
OUT_FILENAME = 'result.csv'


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

# withを使用せず記述した場合
fw = open(OUT_FILENAME, 'w', encoding='utf-8')
print(title.strip()+',合計', file=fw)                   # 1行目を生成して出力

# 一人分ずつ合計を求める
for data in person_data:                                # 各人のデータを1人分ずつ処理
    name, scores_str = data[0], data[1:]                # 名前と得点に分ける
    # scores = [int(num) for num in scores_str]         # 文字列を数字に変換 内包表記を使用
    scores = list2int(scores_str)                       # 文字列を数字に変換 過去に作った関数を使用
    total = sum(scores)                                 # 合計を求める
    scores_csv = ','.join(map(str, scores))             # flat なcsv文字列に変換
    print(name, scores_csv, total, sep=',', file=fw)    # 一人分ずつ出力

fw.close()

# withを使用した場合
with open(OUT_FILENAME, 'w', encoding='utf-8') as fw:
    print(title.strip()+',合計', file=fw)                # 1行目を生成して出力

    # 一人分ずつ合計を求める
    for data in person_data:                             # 各人のデータを1人分ずつ処理
        name, scores_str = data[0], data[1:]             # 名前と得点に分ける
        # scores = [int(num) for num in scores_str]      # 文字列を数字に変換 内包表記を使用
        scores = list2int(scores_str)                    # 文字列を数字に変換 過去に作った関数を使用
        total = sum(scores)                              # 合計を求める
        scores_csv = ','.join(map(str, scores))          # flat なcsv文字列に変換
        print(name, scores_csv, total, sep=',', file=fw) # 一人分ずつ出力
