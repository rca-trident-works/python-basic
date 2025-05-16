string2int = __import__('string2int').string2int

def main():
    # Test cases (input, expected output)
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
        # Passed!: input_str, result
        # Failed!: input_str, expected, result
        if result == expected:
            print(f"✅️ Passed!: {input_str} (Type: {type(input_str)}) -> Got: {result} (Type: {type(result)})")
        else:
            print(f"❌️ Failed!: {input_str} (Type: {type(input_str)}) -> Expected: {expected} (Type: {type(expected)}), Got: {result} (Type: {type(result)})")

if __name__ == "__main__":
    main()
