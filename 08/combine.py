def combine_list(list1, list2):
    """
    Combine two lists into a single list.
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1 + list2

def test_combine_list():
    """
    Test the combine_list function.
    """
    test_cases = [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [], []),
        ([1], [2], [1, 2]),
        ([None], [None], [None, None]),
        ([1, 2], None, ValueError),
        (None, [1, 2], ValueError),
    ]

    for list1, list2, expected in test_cases:
        if isinstance(expected, type) and issubclass(expected, Exception):
            try:
                result = combine_list(list1, list2)
                print(f"❌️ Failed!: {list1}, {list2} -> Expected an exception but got: {result}")
            except expected as e:
                print(f"✅️ Passed!: {list1}, {list2} -> Caught expected exception: {e}")
        else:
            result = combine_list(list1, list2)
            if result == expected:
                print(f"✅️ Passed!: {list1}, {list2} -> Got: {result}")
            else:
                print(f"❌️ Failed!: {list1}, {list2} -> Expected: {expected}, Got: {result}")


def main():
    # Run the test function
    test_combine_list()

if __name__ == "__main__":
    main()
