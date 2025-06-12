def str2int(string):
    """
    str2int 文字列を数値に変換した値を返す
    - 数字文字列を受け取り、数値（整数）に変換して返す
    - 文字列でない場合は、そのまま値を返す
    - 数値に変換できない場合は0を返す
    - 負の数値も適切に処理する
    """
    if isinstance(string, str):
        # 負の数値の処理を含む
        try:
            return int(string)
        except ValueError:
            return 0        
    else:
        return string


def list2int(string_list):
    """
    list2int 文字列を数値に変換した値を返す（List対応）
    - リストを渡した場合、全ての要素の文字列を数値（整数）に変換して返す
        - 要素が文字列でない場合は、0とする
    - リストでなはなく文字列の場合は、受け取った値を数値に変換して返す
    - リストでもなく、文字列でもない場合は、Noneを返す
    """
    if isinstance(string_list, str):
        return str2int(string_list)
    elif isinstance(string_list, list):
        result = [str2int(i) for i in string_list]
        return result
    else:
        return None

# main
print(list2int(['5', 'ab', '100', 10, 1]))  # 通常のケース
print(list2int('100'))  # 文字列のケース
print(list2int('xyz'))  # 数値に変換できない文字列
print(list2int(['-5', '0', '123']))  # 負の数値と0を含むケース
print(list2int([]))  # 空リストのケース
print(list2int(None))  # Noneのケース
print(list2int(123))  # 数値のケース
