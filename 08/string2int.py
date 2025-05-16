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

