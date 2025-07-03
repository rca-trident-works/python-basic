import getopt
import sys


print(f"引数の個数 {len(sys.argv)}")


opts, args = getopt.getopt(
    sys.argv[1:],
    "cmlLw",
    ["bytes", "chars", "lines",  "max-line-length", "words", "help", "version"])


print("Options:", opts)
print("Arguments:", args)
