import unicodedata

def is_katakana(text):
    """
    文字列がカタカナのみで構成されているか判定する関数
    """
    for char in text:
        if not unicodedata.name(char).startswith('KATAKANA'):
            return False
    return True

def add_fruit(fruits, input_str):
    """
    フルーツリストに新しい果物を追加する関数
    """
    if not is_katakana(input_str):
        print("入力された文字列はカタカナでないようです。")
        return
    if len(fruits) >= 100:
        print("リストの長さが最大値に達しました。新しい果物は追加できません。")
        return
    if input_str in fruits:
        print(f"{input_str}は、知っています！")
    else:
        print(f"{input_str}は、知りませんでした。覚えておきます。")
        fruits.append(input_str)


def main():
    fruits = ['バナナ', 'リンゴ', 'オレンジ']
    while True:
        input_str = input("果物をカタカナで入力してください：")
        if input_str == '':
            break
        add_fruit(fruits, input_str)

    print('知っている果物')
    print(fruits)


if __name__ == "__main__":
    main()
