import sys
import windows_argv

# wildcardのwindows用処理
windows_argv.sys_argv()

# ファイルのエンコーディングを指定
file_encoding = "utf_8"

argv = sys.argv
if len(argv) >= 2:
    total_line_count = 0
    total_word_count = 0
    total_char_count = 0
    total_byte_count = 0

    for filename in argv[1:]:
        with open(filename, encoding=file_encoding) as f:
            line_count = 0
            word_count = 0
            char_count = 0
            byte_count = 0
            for line in f:
                line_count += 1
                word_count += len(line.split())
                # 文字数なのか？バイト数なのか？
                char_count += len(line)
                byte_count += len(line.encode(file_encoding))
        print(f"{line_count:3} {word_count:3} {byte_count:3} {filename}")
        total_line_count += line_count
        total_word_count += word_count
        total_char_count += char_count
        total_byte_count += byte_count
    if len(argv) >= 3:
        print(f"{total_line_count:3} {total_word_count:3} {total_byte_count:3} 合計")
