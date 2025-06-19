import os

def main():
    input_directory = input("ファイルとディレクトリを一覧表示するディレクトリのパスを入力してください: ")

    if not input_directory:
        print("ディレクトリのパスは空にできません。")
        return

    if not os.path.isdir(input_directory):
        print(f"ディレクトリ '{input_directory}' は見つかりません。")
        return

    # ディレクトリ'./'内の項目:
    # - ren1_2.py
    # - ren1_3.py
    # ↑こんな感じ

    try:
        items = os.listdir(input_directory)
        if not items:
            print(f"ディレクトリ '{input_directory}' は空です。")
            
        else: 
            print(f"ディレクトリ '{input_directory}' の内容:")
            for item in items:
                print(f"- {item}")
    except PermissionError:
        print(f"ディレクトリ '{input_directory}' の内容を表示する権限がありません。")

if __name__ == "__main__":
    main()
