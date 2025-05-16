
str2list = __import__('ren2_1').str2list
list2int = __import__('string2int').list2int

def get_even(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    int_list = list2int(str2list(s))
    even_list = [x for x in int_list if x % 2 == 0]
    return even_list

def main():
    print("空白で区切られた整数を入力してください: ")
    input_str = input()

    # 偶数のリストを取得
    try:
        result = get_even(input_str)
        print("Result: ", result)
    except ValueError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()

