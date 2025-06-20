import sys
import os

if len(sys.argv) < 2:
    print(f"使用方法: python {os.path.basename(__file__)} <名前>")
else:
    name = sys.argv[1]
    print(f"こんにちは、{name}さん！")
