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
        
def save_words(words):
    with open(path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(f"{word}\n")

def to_string(arr):
    return "[" + ", ".join(arr) + "]"

def main():
    words = load_words()
    while True:
        scan_word = input("単語を入力してください: ")
        if scan_word == "":
            print("終了します")
            print("これまでに覚えた単語: " + to_string(words))
            save_words(words)
            break
        elif scan_word == "LIST":
            print("単語リスト:" + to_string(words))
        elif scan_word in words:
            print("すでに登録済みです")
        else:
            words.append(scan_word)

if __name__ == "__main__":
    main()
