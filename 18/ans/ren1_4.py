import collections
import re
import glob


FOLDER = 'html'
file_list = glob.glob(f"{FOLDER}/*")
print(file_list)    # 念の為出力
pattern = r'"(https?://.+?)"'

for filename in file_list:
    print(f'\n[Filename]:{filename}')
    with open(filename, 'r', encoding='utf8') as f:
        contents = f.read()
        result = re.findall(pattern, contents)

    print("-="*10)

    # モジュールを使用した場合
    count_result = collections.Counter(result)
    data_count = 0
    for (url, cnt) in count_result.most_common():
        if cnt == 1:
            break
        print(f'{cnt} - {url}')
        data_count += 1
        if data_count >= 10:
            break
    print("-="*10)
