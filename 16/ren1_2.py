import os

def main():
    input_directory = input("作成するディレクトリ名を入力してください: ")

    if not input_directory:
        print("ディレクトリ名は空にできません。")
        return
    if os.path.exists(input_directory):
        print(f"ディレクトリ '{input_directory}' はすでに存在します。")
        return
    if input_directory.startswith('/'):
        print("絶対パスは使用できません。相対パスを指定してください。")
        return

    try:
        os.makedirs(input_directory)
        print(f"ディレクトリ '{input_directory}' を作成しました。")
    except FileExistsError:
        print(f"ディレクトリ '{input_directory}' はすでに存在します。")
    except PermissionError:
        print(f"ディレクトリ '{input_directory}' を作成する権限がありません。")
    except Exception as e:
        print(f"ディレクトリ '{input_directory}' の作成中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
