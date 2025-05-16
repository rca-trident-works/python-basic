str2list = __import__('ren2_1').str2list

def even_list(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    words = str2list(s)
    even_words = words[1::2] # 1番目から2つ飛ばしで取得(0番目の要素を1とみなすため)
    return even_words

def main():
    print("空白で区切られた文字列を入力してください: ")
    input_str = input()

    # 偶数番目の単語を取得
    try:
        result = even_list(input_str)
        print("Result: ", result)
    except ValueError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()

