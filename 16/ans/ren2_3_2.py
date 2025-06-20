import sys
import os

if len(sys.argv) < 2:
    print(f"使用方法: python {os.path.basename(__file__)} <ファイルパス>")
else:
    file_path = sys.argv[1]
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
            for line_no, line in enumerate(content, 1):
                print(f"{line_no}:{line.rstrip()}")
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりません。")
    except UnicodeDecodeError:
        print(f"ファイル '{file_path}' のエンコーディングが正しくありません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

