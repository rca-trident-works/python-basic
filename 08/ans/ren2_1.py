def str2list(string):
    """文字列をリストに変換。区切り文字はスペース"""
    if not isinstance(string, str):
        raise ValueError("文字列を入力してください")
    
    # 空文字列やスペースのみの入力をチェック
    if not string.strip():
        raise ValueError("有効な文字列を入力してください")
    
    return string.split()


# main
try:
    keyin = input('空白で区切られた文字列を入力してください：')
    result = str2list(keyin)
    print(result)
except ValueError as e:
    print(f"エラー: {e}")
