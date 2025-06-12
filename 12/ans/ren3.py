DATA_FILENAME = 'word.txt'

# readline版
with open(DATA_FILENAME) as f:
    line_number = 1
    for line in f:
        print(f'{line_number:04d}:{line.strip()}')
        line_number += 1

# readlines版
with open(DATA_FILENAME) as f:
    word_lists = f.readlines()
    for line_number, line in enumerate(word_lists):
        print(f'{line_number+1:04d}:{line.strip()}')
