import os

new_directory = input("作成するディレクトリ名を入力してください: ")
os.makedirs(new_directory, exist_ok=True)
print(f"ディレクトリ '{new_directory}' を作成しました。")

