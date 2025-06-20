import sys
import os

if len(sys.argv) < 2:
    print(f"使用方法: python {os.path.basename(__file__)} <数値1> <数値2> ...")
else:
    numbers = list(map(float, sys.argv[1:]))
    average = sum(numbers) / len(numbers)
    print(f"数値リストの平均: {average}")

    # numbers = [float(n) for n in sys.argv[1:]]
