import sys
import os

if len(sys.argv) < 2:
    print(f"使用方法: python {os.path.basename(__file__)} <ディレクトリパス>")
else:
    directory_path = sys.argv[1]
    try:
        files = os.listdir(directory_path)
        print(f"ディレクトリ '{directory_path}' 内のファイル一覧:")
        for file in files:
            print(f" - {file}")
    except FileNotFoundError:
        print(f"ディレクトリ '{directory_path}' が見つかりません。")
    except NotADirectoryError:
        print(f"'{directory_path}' はディレクトリではありません。")
    except PermissionError:
        print(f"ディレクトリ '{directory_path}' へのアクセス権がありません。") 