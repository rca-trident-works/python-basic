# 初期化
marks = ('S', 'H', 'C', 'D')  # 4種類のマーク
cards = []                  # デッキ用リスト

# loopで作成する方法
for m in marks:
    for i in range(13):
        cards.append((m, i+1))
    # for i in range(1,14):
    #     cards.append((m, i))

print('-'*10)
print(cards)
print('-'*10)

# 内包表記1
cards = [(m, i+1) for i in range(13) for m in marks]
print(cards)
print('-'*10)

# 内包表記2
cards = [(m, i+1) for m in marks for i in range(13)]
print(cards)
print('-'*10)

# 1枚選択
import random # 乱数用モジュール
r = random.randrange(52) # 0〜51の乱数生成
print(f'選んだカードは{cards[r]}です')
