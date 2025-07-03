import getopt
import sys


print(f"引数の個数 {len(sys.argv)}")


opts, args = getopt.getopt(
    sys.argv[1:],
    "abcdef:",
    ["vvv", "www", "xxx",  "yyy", "zzz="])


print("Options:", opts)
print("Arguments:", args)
