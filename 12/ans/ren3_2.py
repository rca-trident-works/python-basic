import os
DATAFILE = 'word.txt'

if os.path.isfile(DATAFILE):
    with open(DATAFILE) as f:
        line_number = 1
        for line in f:
            print(f'{line_number:04d}:{line.strip()}')
            line_number += 1
else:
    print(f'{DATAFILE}がありません')
