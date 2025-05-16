def str2list(s):
    """
    Convert a string to a list of characters.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    # Split by whitespace and convert to list
    return list(s.split())

def test_str2list():
    """
    Test the str2list function.
    """
    test_cases = [
        ("hello world", ['hello', 'world']),
        ("", []),
        ("a b c", ['a', 'b', 'c']),
        (None, ValueError),
        (123, ValueError),
    ]

    for input_str, expected in test_cases:
        if isinstance(expected, type) and issubclass(expected, Exception):
            try:
                result = str2list(input_str)
                print(f"❌️ Failed!: {input_str} -> Expected an exception but got: {result}")
            except expected as e:
                print(f"✅️ Passed!: {input_str} -> Caught expected exception: {e}")
        else:
            result = str2list(input_str)
            if result == expected:
                print(f"✅️ Passed!: {input_str} -> Got: {result}")
            else:
                print(f"❌️ Failed!: {input_str} -> Expected: {expected}, Got: {result}")

def main():
    # Run the test function
    test_str2list()

if __name__ == "__main__":
    main()
