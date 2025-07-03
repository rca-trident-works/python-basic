import re
from pprint import pprint


def output_file(filename, data):
    '''ファイルに配列を出力する
        1行目にはデータ件数
        2行目以降にデータ
    '''
    with open(filename, 'w', encoding='utf8') as f:
        f.write(f"データ件数：{len(data)}\n")
        f.writelines([d+"\n" for d in data])


# main
DATA_FILENAME = 'data.csv'
ERROR_FILENAME = 'error_tel.txt'
RESULT_FILENAME = 'tel_list.txt'

re_pattern = r'^\(?(0\d{1,4})[-\(\)]?(\d{1,4})[\)-]?(\d{4})$'
try:
    with open(DATA_FILENAME, 'r', encoding='utf8') as f:
        header = f.readline().strip()
        columns = header.split(',')
        columns_num = len(columns)

        # 格納用リスト
        error_data = []
        result_data = []

        data = f.readlines()
        for line in data:
            line = line.strip()
            cols = line.split(',')

            # カラム数のチェックを先に行う
            if len(cols) != columns_num:
                # 異常データ行は無視
                continue

            temp = dict(zip(columns, cols))

            # 電話番号が正しいか？
            match_data = re.match(re_pattern, temp['電話番号'])
            if match_data == None:
                error_data.append(
                    f"{temp['No']},{temp['名前']},{temp['電話番号']},{temp['携帯']}")
                continue

            # temp['電話番号'] = match_data.group(1)+match_data.group(2)+match_data.group(3)
            temp['電話番号'] = ''.join(match_data.groups())

            # 携帯番号が正しいか？
            match_data = re.match(re_pattern, temp['携帯'])
            if match_data == None:
                error_data.append(
                    f"{temp['No']},{temp['名前']},{temp['電話番号']},{temp['携帯']}")
                continue
            temp['携帯'] = ''.join(match_data.groups())

            # すべて正常なデータは追加
            result_data.append(
                f"{temp['No']},{temp['名前']},{temp['電話番号']},{temp['携帯']}")

    output_file(ERROR_FILENAME, error_data)
    output_file(RESULT_FILENAME, result_data)
except Exception as e:
    print(f"ファイル読み込みエラー: {DATA_FILENAME} ({e})")
    exit(1) 