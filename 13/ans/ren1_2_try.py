file_name = input("ファイル名を入力してください: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_name}が存在しません")
except IOError:
    print(f"{file_name}の読み取りに失敗しました")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
