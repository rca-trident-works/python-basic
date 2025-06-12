def str2int(string):
    """
    str2int 文字列を数値に変換した値を返す
    - 数字文字列を受け取り、数値（整数）に変換して返す 
    - 文字列でない場合は、そのまま値を返す
    - 数値に変換できない場合は0を返す
    """
    if isinstance(string, str):
    # if type(string) is str: でも同じ動作
        if string.isnumeric():
            return int(string)
        else:
            return 0
    else:
        return string


# main
print(str2int('a'))
print(str2int('10'))
print(str2int(100))
