import os

# Static
path = "./word.txt"

def load_words():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
        return words
    else:
        return []


def main():
    words = load_words()

    count = 0

    for word in words:
        count += 1
        print(f"{count:04}:{word}")

if __name__ == "__main__":
    main()
