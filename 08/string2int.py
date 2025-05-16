# Plugin for converting a string to an integer

def string2int(s):
    # if s is not a string, return s directly
    if not isinstance(s, str):
        return s

    # if s is empty, return 0
    if s == "":
        return 0

    try:
        # Try to convert the string to an integer
        return int(s)
    except ValueError:
        # If conversion fails, return 0
        return 0

def test_string2int():
    # Test cases
    test_cases = [
        ("123", 123),
        ("-123", -123),
        ("0", 0),
        ("abc", 0),
        ("", 0),
        (None, None),
        (123, 123),  # Non-string input
    ]

    for input_str, expected in test_cases:
        result = string2int(input_str)
        if result == expected:
            print(f"✅️ Passed!: {input_str} -> Got: {result}")
        else:
            print(f"❌️ Failed!: {input_str} -> Expected: {expected}, Got: {result}")

def main():
    # Run the test function
    test_string2int()

if __name__ == "__main__":
    main()
