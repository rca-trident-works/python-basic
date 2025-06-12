# 読み込み
filename_utf8 = 'foo.csv'
with open(filename_utf8, 'r', encoding='utf8') as f:
    # 1行目のみ読み込む
    line_utf8 = f.readline()

filename_bom = 'foo_bom.csv'
with open(filename_bom, 'r', encoding='utf8') as f:
    # 1行目のみ読み込む
    line_bom = f.readline()

# 比較できるように出力
print('utf8でopenした場合')
print(f'{filename_utf8:<14}',list(line_utf8))
print(f'{filename_bom:<14}',list(line_bom))
print()

with open(filename_utf8, 'r', encoding='utf_8_sig') as f:
    # 1行目のみ読み込む
    line_utf8 = f.readline()

with open(filename_bom, 'r', encoding='utf_8_sig') as f:
    # 1行目のみ読み込む
    line_bom = f.readline()

print('utf_8_sigでopenした場合')
print(f'{filename_utf8:<14}',list(line_utf8))
print(f'{filename_bom:<14}',list(line_bom))
