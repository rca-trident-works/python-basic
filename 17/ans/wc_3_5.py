import os
import getopt
import glob
import sys


def usage():
    print(f"詳しくは '{os.path.basename(__file__)} --help' を実行して下さい。")
    sys.exit()


def version():
    print(
        """
wc (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
ライセンス GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

作者 Paul Rubin および David MacKenzie。
"""
    )
    sys.exit()


def help():
    print(
        """
使用法: wc [OPTION]... [FILE]...
または: wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

FILE の指定がなかったり, - であった場合, 標準入力から読み込みます.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --help     この使い方を表示して終了する
      --version  バージョン情報を表示して終了する

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
wc の翻訳に関するバグは <http://translationproject.org/team/ja.html> に連絡してください。
Full documentation at: <http://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation'
"""
    )
    sys.exit()


def check_encoding(filename):
    """
    ファイルのエンコーディングをチェックする関数。
    単純にUTF-8/cp932を区別している
    """
    file_encoding = "utf_8"  # デフォルトはutf-8とする
    try:
        with open(filename, "r", encoding=file_encoding) as f:
            f.read()  # 読み込みでエンコーディングを確認
        return file_encoding
    except UnicodeDecodeError:
        return "cp932"


def wc_file(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    max_line_length = 0

    # ファイルのエンコーディングをチェック
    file_encoding = check_encoding(filename)
    with open(filename, encoding=file_encoding) as f:
        for line in f:
            # 行数をカウント
            line_count += 1
            # 1行の単語数をカウント
            word_count += len(line.split())
            # 1行の文字数をカウント
            char_count += len(line)
            # 1行のバイト数をカウント
            line_length = len(line.encode(file_encoding))
            byte_count += line_length
            # 最長の行のバイト数をチェック
            if max_line_length < line_length:
                max_line_length = line_length

    return [line_count, word_count, char_count, byte_count, max_line_length]


# main
import windows_argv

windows_argv.sys_argv()

argv = sys.argv

if len(argv) >= 2:
    # オプションの処理
    try:
        opts, args = getopt.getopt(
            argv[1:],
            "cmlLw",
            ["bytes", "chars", "lines", "max-line-length", "words", "help", "version"],
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # option処理（flag設定）
    flag_c = flag_m = flag_l = flag_L = flag_w = False
    for opt, arg in opts:
        if opt in ("--help"):
            help()
        elif opt in ("--version"):
            version()
        elif opt in ("-c", "--bytes"):
            flag_c = True
        elif opt in ("-m", "--chars"):
            flag_m = True
        elif opt in ("-l", "--lines"):
            flag_l = True
        elif opt in ("-L", "--max-line-length"):
            flag_L = True
        elif opt in ("-w", "--words"):
            flag_w = True

    if flag_c == flag_m == flag_l == flag_L == flag_w == False:
        flag_c = True
        flag_m = True
        flag_l = True

    total_line_count = 0
    total_word_count = 0
    total_char_count = 0
    total_byte_count = 0
    max_line_length = 0

    for filename in argv[1:]:
        [line_count,
         word_count, 
         char_count, 
         byte_count,
         max_line_length] = wc_file(filename)

        print(f"{line_count:3} {word_count:3} {char_count:3} {filename}")
        total_line_count += line_count
        total_word_count += word_count
        total_char_count += char_count
        total_byte_count += byte_count
    if len(argv) >= 3:
        print(f"{total_line_count:3} {total_word_count:3} {total_char_count:3} 合計")
else:
    usage()
