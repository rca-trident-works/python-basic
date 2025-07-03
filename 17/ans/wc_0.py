import sys

# ファイルのエンコーディングを指定
file_encoding = "utf_8"

argv = sys.argv
if len(argv) >= 2:
    total_line_count = 0
    total_word_count = 0
    total_char_count = 0

    for filename in argv[1:]:
        with open(filename, encoding=file_encoding) as f:
            line_count = 0
            word_count = 0
            char_count = 0
            for line in f:
                # 行のカウント
                line_count += 1
                # 単語数のカウント
                pass
                # 文字数のカウント
                pass
        print(f"{line_count:3} {word_count:3} {char_count:3} {filename}")
        total_line_count += line_count
        total_word_count += word_count
        total_char_count += char_count
    if len(argv) >= 3:
        print(f"{total_line_count:3} {total_word_count:3} {total_char_count:3} 合計")
