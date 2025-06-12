import math
PAYMENT_UNIT = 100 # 100円単位で処理する場合
MIN_PARTICIPANTS = 2

def input_int(message: str) -> int:
    """
    messageを表示し、入力値をintで返す。
    数値以外の場合は、0を返す
    """
    try:
        return int(input(f"{message}を入力してください："))
    except ValueError:
        return 0


def calc_payment(total: int, num_people: int) -> list[int]:
    """
    合計額と人数から、割り勘金額を計算する。
    戻り値は、一般参加者の金額と幹事の金額をリストで返す
    """
    unit = PAYMENT_UNIT
    if num_people < MIN_PARTICIPANTS:
        print("人数が正しくありません")
        return [0, total]
    pay_people = total // num_people
    pay_people = math.ceil(pay_people / unit) * unit
    pay_coordinator = total - pay_people * (num_people - 1)
    return [pay_people, pay_coordinator]


def output_payment(pay_people: int, pay_coordinator: int, num_people: int) -> None:
    """
    支払い情報を出力する
    
    Args:
        pay_people (int): 一般参加者の支払金額
        pay_coordinator (int): 幹事の支払金額
        num_people (int): 参加人数
    """
    print(f"支払金額：{pay_people:,}円 ({num_people-1}人)")
    print(f"幹事金額：{pay_coordinator:,}円")


# main
total = input_int("支払合計金額")
if total <= 0:
    print("金額が正しくありません")
    exit(1)
num_people = input_int("参加者人数")
if num_people < MIN_PARTICIPANTS:
    print("人数が正しくありません")
    exit(1)

pay_people, pay_coordinator = calc_payment(total, num_people)
output_payment(pay_people, pay_coordinator, num_people)
