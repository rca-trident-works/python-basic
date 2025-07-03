import argparse
import sys


print(f"引数の個数 {len(sys.argv)}")

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--bytes', help='バイト数を表示する', action='store_true')
parser.add_argument('-m', '--chars', help='文字数を表示する', action='store_true')
parser.add_argument('-l', '--lines', help='改行の数を表示する', action='store_true')
parser.add_argument('-L', '--max-line-length',
                    help='最も長い行の長さを表示する', action='store_true')
parser.add_argument('-w', '--words', help='単語数を表示する', action='store_true')
parser.add_argument('--version', help='バージョン情報を表示して終了する', action='store_true')

args = parser.parse_args()

print("Arguments:", args)
