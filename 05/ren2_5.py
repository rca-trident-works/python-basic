# ユーザーに文字列を入力させ、その文字列を逆順に出力する

user_input = input("文字列を入力してください: ")

reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("逆順の文字列は:", reversed_string)

# Sliceで処理
reversed_string = user_input[::-1]
print("逆順の文字列は:", reversed_string)
