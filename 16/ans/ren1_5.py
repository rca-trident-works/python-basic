import os

directory_path = input("ファイルとディレクトリを一覧表示するディレクトリのパスを入力してください: ")
if os.path.isdir(directory_path):
    items = os.listdir(directory_path)
    print(f"ディレクトリ '{directory_path}' 内の項目:")
    for item in items:
        print(f" - {item}")
else:
    print(f"ディレクトリ '{directory_path}' が見つかりません。")
