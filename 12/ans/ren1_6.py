import locale
import datetime
import platform

year = 2024
month = 5
day = 22

# ここにコードを書いてください
if platform.system() == 'Windows':
    locale.setlocale(locale.LC_TIME, 'ja_JP')
    # locale.setlocale(locale.LC_TIME, 'Japanese_Japan.932')
else:
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    
dw = datetime.date(year, month, day).strftime('%a')
formatted_date = f'日付: {year}年{month}月{day}日({dw})'
print(formatted_date)
