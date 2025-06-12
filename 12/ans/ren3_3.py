import os
DATAFILE = 'word.txt'

try:
    with open(DATAFILE) as f:
        line_number = 1
        for line in f:
            print(f'{line_number:04d}:{line.strip()}')
            line_number += 1
except FileNotFoundError:
    print(f'{DATAFILE}がありません')
except Exception as e:
    print(f'エラーが発生しました: {e}') 