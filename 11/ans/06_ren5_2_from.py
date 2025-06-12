from random import randrange, shuffle
# 乱数用モジュールからrandrange,shuffleのみimport

# 初期化
marks = ('S', 'H', 'C', 'D')  # 4種類のマーク
cards = []                    # デッキ用リスト

for m in marks:
    for i in range(13):
        cards.append((m, i+1))

print('-'*10)
print(cards)
print('-'*10)

# 1枚選択
r = randrange(52)      # 0〜51の乱数生成
print(f'選んだカードは{cards[r]}です')

shuffle(cards)
print('-'*10)
print(cards)
print('-'*10)
