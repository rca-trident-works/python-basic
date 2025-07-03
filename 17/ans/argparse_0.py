import argparse
import sys


print(f"引数の個数 {len(sys.argv)}")

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--aaa')
parser.add_argument('-b', '--bbb')
parser.add_argument('-c', '--ccc')
parser.add_argument('-d', '--ddd')
parser.add_argument('-e', '--eee')
parser.add_argument('-f', '--fff')

args = parser.parse_args()

print("Arguments:", args)
