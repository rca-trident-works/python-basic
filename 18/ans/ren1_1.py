import re

FILENAME = 'Yahoo.html'

pattern = r'"(https?://.+?)"'
# pattern = r'"(https?://[^"]+)"'

with open(FILENAME, 'r', encoding='utf8') as f:
    contents = f.read()
    result = re.findall(pattern, contents)

for idx, string in enumerate(result):
    print(f'{idx} - {string}')
