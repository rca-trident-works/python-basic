import os
import getopt
import sys


def usage():
    """使い方の表示"""
    print(f"詳しくは '{os.path.basename(__file__)} --help' を実行して下さい。")
    sys.exit()


def version():
    """バージョン情報の表示"""
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
    """Helpのメッセージ表示"""
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


def wc_file(filename) -> dict:
    """ファイルの各種情報を調べ、辞書で返す"""
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    max_line_length = 0

    # ファイルのエンコーディングをチェック
    try:
        file_encoding = check_encoding(filename)
        with open(filename, encoding=file_encoding) as f:
            for line in f:
                # -l:行数をカウント
                line_count += 1
                # -w:1行の単語数をカウント
                word_count += len(line.split())
                # -c:1行のバイト数
                byte_count_temp = len(line.encode(file_encoding))
                # -c:1行のバイト数をカウント
                byte_count += byte_count_temp
                # -m:1行の文字数をカウント
                char_count += len(line)
                # -L:最大の行の長さ用（表示桁数）
                line_length_temp = len(line.rstrip().encode('utf_8'))//3 * 2
                if max_line_length < line_length_temp:
                    max_line_length = line_length_temp
    except FileNotFoundError as e:
        print(f"wc: '{e.filename}': そのようなファイルやディレクトリはありません")
        sys.exit()

    # 結果を辞書で返す
    return dict(
        line=line_count,
        word=word_count,
        char=char_count,
        byte=byte_count,
        max_length=max_line_length,
    )


def output(info_stack, flags):
    """ファイル情報一覧をflagに基づいて出力
    最大の桁数に合わせて整形
    """
    width_l = width_w = width_m = width_c = width_L = 0

    for filename, info in info_stack:
        width_l = max(width_l, len(str(info["line"])))
        width_w = max(width_w, len(str(info["word"])))
        width_m = max(width_m, len(str(info["char"])))
        width_c = max(width_c, len(str(info["byte"])))
        width_L = max(width_L, len(str(info["max_length"])))

    for filename, info in info_stack:
        if flags["l"]:
            print(f"{info['line']:{width_l}} ", end="")
        if flags["w"]:
            print(f"{info['word']:{width_w}} ", end="")
        if flags["m"]:
            print(f"{info['char']:{width_m}} ", end="")
        if flags["c"]:
            print(f"{info['byte']:{width_c}} ", end="")
        if flags["L"]:
            print(f"{info['max_length']:{width_L}} ", end="")
        print(f"{filename}")


# main
import windows_argv

windows_argv.sys_argv()
sys_argv = sys.argv

if len(sys_argv) >= 1:
    # オプションの処理
    try:
        # '-'は実装しない
        opts, args = getopt.getopt(
            sys_argv[1:],
            "cmlLw",
            ["bytes", "chars", "lines", "max-line-length", "words", "help", "version"],
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # オプションの処理（flag設定）
    flags = dict.fromkeys(["c", "m", "l", "L", "w"], False)
    # flags = dict(c=False, m=False, l=False, L=False, w=False)
    # flags = {'c': False, 'm': False, 'l': False, 'L': False, 'w': False}
    for opt, arg in opts:
        if opt in ("--help"):
            help()
        elif opt in ("--version"):
            version()
        elif opt in ("-c", "--bytes"):
            flags["c"] = True
        elif opt in ("-m", "--chars"):
            flags["m"] = True
        elif opt in ("-l", "--lines"):
            flags["l"] = True
        elif opt in ("-L", "--max-line-length"):
            flags["L"] = True
        elif opt in ("-w", "--words"):
            flags["w"] = True

    # オプション省略時(default)
    if sum(flags.values()) == 0:
        flags["l"] = True  # 行数
        flags["w"] = True  # 単語数
        flags["c"] = True  # バイト数

    # ファイル数が2つ以上の場合の合計出力用
    total_line_count = 0
    total_word_count = 0
    total_char_count = 0
    total_byte_count = 0
    total_max_length = 0

    info_stack = []  # 各ファイル毎の情報をためておくリスト
    # [ファイル名,dict()]
    for filename in args:
        # 各ファイルの情報を取得
        info = wc_file(filename)
        info_stack.append([filename, info])

        # 合計出力用の処理
        total_line_count += info["line"]
        total_word_count += info["word"]
        total_char_count += info["char"]
        total_byte_count += info["byte"]
        if total_max_length < info["max_length"]:
            total_max_length = info["max_length"]

    if len(info_stack) >= 2:
        # ファイル名を「合計」として、同様に追加
        info_stack.append(
            [
                "合計",
                dict(
                    line=total_line_count,
                    word=total_word_count,
                    char=total_char_count,
                    byte=total_byte_count,
                    max_length=total_max_length,
                ),
            ]
        )
else:
    usage()

output(info_stack, flags)
