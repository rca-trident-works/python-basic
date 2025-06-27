import re

FILENAME = 'Yahoo.html'

pattern = r'"(https?://.+?)"'
with open(FILENAME, 'r', encoding='utf8') as f:
    contents = f.read()
    result = re.findall(pattern, contents)

for idx, url in enumerate(result):
    print(f'{idx} - {url}')

# ここまでren1_1.py
print("-="*10)

# モジュールを使用した場合
import collections
count_result = collections.Counter(result)
for (url, cnt) in count_result.most_common():
    # most_common()は多い方からになる(降順sort)
    if cnt == 1:
        break
    print(f'{cnt} - {url}')
print("-="*10)

# モジュールを使用しない場合
count_result = {}
for url in result:
    count_result[url] = count_result.get(url, 0) + 1
    # 上と同じ処理
    # if url in count_result:
    #     count_result[url] += 1
    # else:
    #     count_result[url] = 1

# sort
count_result_sorted = sorted(count_result.items(), key=lambda x: x[1], reverse=True)
for (url, cnt) in count_result_sorted:
    if cnt == 1:
        break
    print(f'{cnt} - {url}')
