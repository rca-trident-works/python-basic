import os

new_directory = input("作成するディレクトリ名を入力してください: ")
try:
    os.makedirs(new_directory, exist_ok=True)
    print(f"ディレクトリ '{new_directory}' を作成しました。")
except Exception as e:
    print(f"ディレクトリの作成中にエラーが発生しました: {e}") 

# 上記だけで良いのか？

# パス・トラバーサル攻撃を想定する
# if '../' in new_directory:
#     print(f'上位ディレクトリへの作成はできません')
# if new_directory[0] == '/':  # linux
#     print(f'絶対パスの指定はできません')
# if ':' in new_directory:  # windows
#     print(f'絶対パスの指定はできません')