def str2list(string):
    """
    文字列をリストに変換。区切り文字はスペース
    """
    if not isinstance(string, str):
        raise ValueError("文字列を入力してください")

    # 空文字列やスペースのみの入力をチェック
    if not string.strip():
        raise ValueError("有効な文字列を入力してください")

    return string.split()


def str2int(string):
    """
    str2int 文字列を数値に変換した値を返す
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
    """
    if isinstance(string_list, str):
        return str2int(string_list)
    elif isinstance(string_list, list):
        result = [str2int(i) for i in string_list]
        return result
    else:
        return None


def get_even(full_list):
    """
    リスト内の偶数（2で割り切れる数）の要素を返す
    """
    if not isinstance(full_list, list):
        raise ValueError("リストを入力してください")

    if not full_list:
        raise ValueError("空のリストは処理できません")

    return [x for x in full_list if x % 2 == 0]


# main
try:
    keyin = input("空白で区切られた整数を入力してください：")
    result = get_even(list2int(str2list(keyin)))
    print(f"偶数要素: {result}")
except ValueError as e:
    print(f"エラー: {e}")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
