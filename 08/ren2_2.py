str2list = __import__('ren2_1').str2list

def word_count(s):
    """
    Count the occurrences of each word in a string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    words = str2list(s)
    # 単語数（結果配列）の長さを取得
    return len(words)

def main():
    print("空白で区切られた文字列を入力してください: ")
    input_str = input()

    # 単語数をカウント
    try:
        result = word_count(input_str)
        print("Result: ", result)
    except ValueError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
