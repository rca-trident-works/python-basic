def str2list(s):
    """
    Convert a string to a list of characters.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    # Split by whitespace and convert to list
    return list(s.split())

def main():
    print("空白で区切られた文字列を入力してください: ")
    input_str = input()

    # Convert the string to a list
    try:
        result = str2list(input_str)
        print("Result: ", result)
    except ValueError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()

