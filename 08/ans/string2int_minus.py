def str2int(string):
    """
    str2int 文字列を数値に変換した値を返す
    - 数字文字列を受け取り、数値（整数）に変換して返す
    - 文字列でない場合は、そのまま値を返す
    - 数値に変換できない場合は0を返す
    - 負の数値も適切に処理する
    """
    if isinstance(string, str):
        # 負の数値の処理
        if string.startswith('-') and string[1:].isnumeric():
            return -int(string[1:])
        # 正の数値の処理
        elif string.isnumeric():
            return int(string)
        else:
            return 0
    else:
        return string


# main
print(str2int('a'))      # 変換不可: 0
print(str2int('10'))     # 正の数: 10
print(str2int(100))      # 非文字列: 100
print(str2int('-10'))    # 負の数: -10
print(str2int(''))       # 空文字列: 0
print(str2int('1.5'))    # 小数点: 0
