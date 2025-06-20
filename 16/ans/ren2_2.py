import sys
import os

if len(sys.argv) < 3:
    print(f"使用方法: python {os.path.basename(__file__)} <数値1> <数値2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    except ValueError:
        print("エラー: 引数は数値である必要があります。")
