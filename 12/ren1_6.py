import locale
import datetime

yaer = 2024
month = 5
day = 22

date = datetime.date(yaer, month, day)
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

formatted_date = f"日付: {date:%Y年%m月%d日(%a)}"
print(formatted_date)
