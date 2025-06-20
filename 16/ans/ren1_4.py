import os

file_path = input("サイズを取得するファイルのパスを入力してください: ")
if os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)
    print(f"ファイル '{file_path}' のサイズは {file_size} バイトです。")
else:
    print(f"ファイル '{file_path}' が見つかりません。")
