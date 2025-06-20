import os

directory_path = input("ファイルとディレクトリを一覧表示するディレクトリのパスを入力してください: ")
try:
    items = os.listdir(directory_path)
    print(f"ディレクトリ '{directory_path}' 内の項目:")
    for item in items:
        print(f" - {item}")
except FileNotFoundError:
    print(f"ディレクトリ '{directory_path}' が見つかりません。")
