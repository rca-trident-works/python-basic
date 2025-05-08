fruits = ['バナナ', 'リンゴ', 'オレンジ']

def print_fruits(fruits):
    res = "知っている果物: " + ", ".join(fruits)
    print("\n" + res)
    
def save_fruits(input_val):
    res = input_val + "は知りませんでした。覚えておきます。"
    print(res)

    fruits.append(input_val)

def validate(input_val):
    # TODO:
    if input_val == "":
        return False
    else:
        return True

def is_contains(input_val, fruits):
    for fruit in fruits:
        if fruit == input_val:
            return True
    return False

def main():
    try:
        while True:
            input_val = input("果物をカタカナで入力してください: ")
            if validate(input_val) == False:
                print("入力が無効です。")
                return
            if is_contains(input_val, fruits):
                print(input_val + "は知っています！")
            else:
                save_fruits(input_val)
    except KeyboardInterrupt:
        print_fruits(fruits)

if __name__ == "__main__":
    main()
