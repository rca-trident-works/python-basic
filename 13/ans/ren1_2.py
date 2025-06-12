file_name = input("ファイル名を入力してください: ")

file = open(file_name, 'r')
if file:
    content = file.read()
    print(content)
    file.close()
else:
    print("ファイルを開くことができませんでした")
