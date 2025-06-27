import collections
import re
import glob
import sys
import os


def usage():
    print("フォルダ名を指定してください")
    print(f"使い方：{os.path.basename(__file__)} folder_name")
    sys.exit()


# main
if len(sys.argv) < 2:
    usage()

folder_name = sys.argv[1]
if os.path.isdir(folder_name) == False:
    usage()

file_list = glob.glob(f"{folder_name}/*")
if file_list:
    pass
else:
    print(f'{folder_name} にファイルがありません')
    usage()

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
        if data_count > 10:
            break
    print("-="*10)
