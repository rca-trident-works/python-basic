import sys

# ファイルのエンコーディングを指定
file_encoding = "utf_8"

def wc_file(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0

    with open(filename, encoding=file_encoding) as f:
        for line in f:
            # 行数をカウント
            line_count += 1
            # 1行の単語数をカウント
            word_count += len(line.split())
            # 1行の文字数をカウント
            char_count += len(line)
            # 1行のバイト数をカウント
            byte_count += len(line.encode(file_encoding))

    return [line_count, word_count, char_count, byte_count]


argv = sys.argv
if len(argv) >= 2:
    total_line_count = 0
    total_word_count = 0
    total_char_count = 0
    total_byte_count = 0

    for filename in argv[1:]:
        [line_count,
         word_count,
         char_count,
         byte_count] = wc_file(filename)

        print(f'{line_count:3} {word_count:3} {byte_count:3} {filename}')
        total_line_count += line_count
        total_word_count += word_count
        total_char_count += char_count
        total_byte_count += byte_count
    if len(argv) >= 3:
        print(
            f'{total_line_count:3} {total_word_count:3} {total_byte_count:3} 合計')
