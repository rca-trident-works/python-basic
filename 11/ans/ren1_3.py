import datetime


def days_since(date_string):
    '''与えられた日時と現在日時の差を求める'''
    # 文字列から日付オブジェクトを作成
    input_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    # 現在の日付を取得
    current_date = datetime.date.today()
    # 経過日数を計算
    delta = current_date - input_date
    return delta.days


# ユーザー入力
user_input = input("日付をYYYY-MM-DD形式で入力してください: ")
print(f"経過日数: {days_since(user_input)}日")
