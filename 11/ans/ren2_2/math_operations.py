def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


if __name__ == '__main__':
    print(add(1, 2))
    print(subtract(3, 4))
    print(multiply(5, 6))
    print(divide(7, 8))
    print(divide(9, 0))
