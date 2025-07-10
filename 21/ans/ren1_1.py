import collections
import re
import sys
import os
import requests


def usage():
    print("URLを指定してください")
    print(f"使い方：{os.path.basename(__file__)} URL")
    sys.exit()


# main
if len(sys.argv) != 2:
    usage()

input_url = sys.argv[1]

try:
    response = requests.get(input_url)
except requests.exceptions.RequestException as e:
    print(f"リクエスト中にエラーが発生しました: {e}")
    sys.exit(1)

if response.status_code != 200:
    print(f"指定したURLが存在しません: {input_url}")
    sys.exit(1)


pattern = r'"(https?://.+?)"'

print(f"\n[URL]:{input_url}")
result = re.findall(pattern, response.text)
# 途中でinteractive modeに入る場合 exit()する
# $ python -i filename
# sys.exit()
print("-=" * 10)

# モジュールを使用した場合
count_result = collections.Counter(result)
data_count = 0
for url, cnt in count_result.most_common():
    print(f"{cnt} - {url}")
    data_count += 1
    if data_count > 10:
        break
print("-=" * 10)
