import os

def main():
    input_file_path = input("サイズを取得するファイルのパスを入力してください: ")

    if not input_file_path:
        print("ファイルのパスは空にできません。")
        return
    
    if not os.path.isfile(input_file_path):
        print(f"ファイル '{input_file_path}' は存在しません。")
        return

    try:
        file_size = os.path.getsize(input_file_path)
        print(f"ファイル '{input_file_path}' のサイズは {file_size} バイトです。")
    except PermissionError:
        print(f"ファイル '{input_file_path}' のサイズを取得する権限がありません。")
    except Exception as e:
        print(f"ファイル '{input_file_path}' のサイズを取得中にエラーが発生しました")

if __name__ == "__main__":
    main()
