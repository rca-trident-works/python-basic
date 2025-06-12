# 与えられた文字列の各文字を大文字に変換して新しい文字列を作成し出力

original_string = "hello world"

uppercase_string = ''.join([char.upper() for char in original_string])
print(uppercase_string)

# 別解
uppercase_string = []
for char in original_string:
    uppercase_string.append(char.upper())
print(''.join(uppercase_string))

# 別解
uppercase_string = ''
for char in original_string:
    uppercase_string += char.upper()
print(uppercase_string)

# 別解
uppercase_string = original_string.upper()
print(uppercase_string)

