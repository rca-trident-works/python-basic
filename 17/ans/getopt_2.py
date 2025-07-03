import getopt
import sys
import os


def usage():
    print(f"詳しくは '{os.path.basename(__file__)} --help' を実行して下さい。")
    sys.exit()


def version():
    print('''
wc (GNU coreutils) 8.32
Copyright (C) 2017 Free Software Foundation, Inc.
ライセンス GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

作者 Paul Rubin および David MacKenzie。
''')
    sys.exit()


def help():
    print('''
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
''')
    sys.exit()


# print(sys.argv)       # 確認用
try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "cmlLw",
        ["help", "version", "words", "max-line-length",
            "bytes", "chars", "lines"]
    )
    # print("Options:", opts)   # 確認用
    # print("Arguments:", args)  # 確認用

except getopt.GetoptError as err:
    print(str(err))
    usage()

# option処理（flag設定）
flag_c = flag_m = flag_l = flag_L = flag_w = False
for opt, arg in opts:
    if opt in ('--help',):
        help()
    elif opt in ('--version',):
        version()
    elif opt in ('-c', '--bytes'):
        flag_c = True
    elif opt in ('-m', '--chars'):
        flag_m = True
    elif opt in ('-l', '--lines'):
        flag_l = True
    elif opt in ('-L', '--max-line-length'):
        flag_L = True
    elif opt in ('-w', '--words'):
        flag_w = True
