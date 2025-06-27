import collections
import re
import sys
import os
import windows_argv


def usage():
    print("ファイル名を指定してください")
    print(f"使い方：{os.path.basename(__file__)} file_name")
    sys.exit()


# main
if len(sys.argv) < 2:
    usage()

windows_argv.sys_argv()
file_list = sys.argv[1:]

pattern = r'"(https?://.+?)"'

for filename in file_list:
    print(f"\n[Filename]:{filename}")
    if os.path.isdir(filename):
        print("ディレクトリなのでSkipします。")
        continue
    try:
        with open(filename, "r", encoding="utf8") as f:
            contents = f.read()
            result = re.findall(pattern, contents)
    except FileNotFoundError:
        print(f"{filename} が見つかりません")
        continue

    print("-=" * 10)

    # モジュールを使用した場合
    count_result = collections.Counter(result)
    data_count = 0
    for url, cnt in count_result.most_common():
        if cnt == 1:
            break
        print(f"{cnt} - {url}")
        data_count += 1
        if data_count > 10:
            break
    print("-=" * 10)
