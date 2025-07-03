import re


def output_file(filename, data):
    '''ファイルに配列を出力する
        1行目にはデータ件数
        2行目以降にデータ
        dataはリストで受け取る
    '''
    try:
        with open(filename, 'w', encoding='utf8') as f:
            f.write(f"データ件数：{len(data)}\n")
            f.writelines([d+"\n" for d in data])
    except Exception as e:
        print(f"ファイル書き込みエラー: {filename} ({e})")


# main
DATA_FILENAME = 'data.csv'
ERROR_FILENAME = 'error_data.txt'
BADPASS_FILENAME = 'bad_password.txt'

re_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)[A-Za-z\d]{8,}$'
# 以下でも可（少し遅くなる）
# re_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'

try:
    with open(DATA_FILENAME, 'r', encoding='utf8') as f:
        header = f.readline().strip()
        columns = header.split(',')
        columns_num = len(columns)

        # 格納用リスト
        error_data = []
        badpass_data = []
        result_data = []

        data = f.readlines()
        for line in data:
            line = line.strip()
            cols = line.split(',')

            # カラム数のチェックを先に行う
            if len(cols) != columns_num:
                error_data.append(line)
                continue

            temp = dict(zip(columns, cols))

            # データに抜けがある場合
            if temp['No'] == '' or temp['名前'] == '' or temp['ユーザ名'] == '':
                error_data.append(line)
                continue

            # パスワードが条件に合わない場合
            if re.match(re_pattern, temp['パスワード']) == None:
                badpass_data.append(
                    f"{temp['No']},{temp['名前']},{temp['ユーザ名']},{temp['パスワード']}")
                continue

            # すべて正常なデータは念の為残しておくだけ
            result_data.append(temp)

    output_file(BADPASS_FILENAME, badpass_data)
    output_file(ERROR_FILENAME, error_data)
except Exception as e:
    print(f"ファイル読み込みエラー: {DATA_FILENAME} ({e})")
    exit(1) 