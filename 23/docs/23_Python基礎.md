# 23 Python基礎

## PythonからExcelを利用する

### openpyxlモジュール

```
$ conda install openpyxl
```

```
$ conda list
```

```
# packages in environment at /home/yoshimura/anaconda3/envs/py39:
#
# Name                     Version          Build              Channel
_libgcc_mutex              0.1              main
_openmp_mutex              5.1              1_gnu
brotlicffi                 1.0.9.2          py39h6a678d5_1
ca-certificates            2025.2.25        h06a4308_0
certifi                    2025.6.15        py39h06a4308_0
cffi                       1.17.1           py39h1fdaa30_1
chardet                    4.0.0            py39h06a4308_1003
charset-normalizer         3.3.2            pyhd3eb1b0_0
et_xmlfile                 1.1.0            py39h06a4308_0
idna                       3.7              py39h06a4308_0
ld_impl_linux-64           2.40             h12ee557_0
libffi                     3.4.4            h6a678d5_1
libgcc-ng                  11.2.0           h1234567_1
libgomp                    11.2.0           h1234567_1
libstdcxx-ng               11.2.0           h1234567_1
libxcb                     1.17.0           h9b100fa_0
ncurses                    6.4              h6a678d5_0
openpyxl                   3.1.5            py39h5eee18b_1
openssl                    3.0.16           h5eee18b_0
pip                        25.1             pyhc872135_2
pthread-stubs              0.3              h0ce48e5_1
pycparser                  2.21             pyhd3eb1b0_0
pysocks                    1.7.1            py39h06a4308_0
python                     3.9.21           he870216_1
readline                   8.2              h5eee18b_0
requests                   2.32.4           py39h06a4308_0
setuptools                 78.1.1           py39h06a4308_0
sqlite                     3.45.3           h5eee18b_0
tk                         8.6.14           h993c535_1
tzdata                     2025b            h04d1e81_0
urllib3                    2.5.0            py39h06a4308_0
wheel                      0.45.1           py39h06a4308_0
xorg-libx11                1.8.12           h9b100fa_1
xorg-libxau                1.0.12           h9b100fa_0
xorg-libxdmcp              1.1.5            h9b100fa_0
xorg-xorgproto             2024.1           h5eee18b_1
xz                         5.6.4            h5eee18b_1
zlib                       1.2.13           h5eee18b_1
```





### 利用方法

```python
import openpyxl
```



> https://openpyxl.readthedocs.io/en/stable/index.html　openpyxl 公式 （英語）
>
> https://qiita.com/sky_jokerxx/items/dc9d8827d946b467ba4b	pythonのopenpyxlの使い方メモ
>
> https://gammasoft.jp/support/how-to-use-openpyxl-for-excel-file/　openpyxl による Excelファイル操作方法のまとめ



### Excelの構造

- workbook
  - worksheet
    - cell
- これらを、オブジェクトとして管理・利用する。



#### workbookの新規作成

```python
import openpyxl

wb = openpyxl.Workbook()
```



#### workbookの読み込み

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
```



#### workbookの保存

```python
import openpyxl

　︙
wb.save("test.xlsx")	# 上書き もしくは　新規保存
wb.save("sample.xlsx")	# 別名保存　もしくは　新規保存
```



【excel1.py】

```python
import openpyxl

wb = openpyxl.Workbook()    # 新規作成
wb.save("test.xlsx")        # test.xlsxで保存

wb = openpyxl.load_workbook("test.xlsx")    # 読み込み
wb.save("sample.xlsx")      # 別名で保存
```



#### worksheetの利用

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")

ws = wb["Sheet1"]		# Sheet1の指定
ws = wb.worksheets[0]	# 先頭のworksheetの指定
ws = wb.active			# activeなworksheetを指定
```



#### worksheetの情報取得・設定

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")

all_sheets = wb.sheetnames	# 存在するworksheet名の取得 ['Sheet1','Sheet2','Sheet3',...]
```



#### worksheetの設定

【excel2.py】

```python
import openpyxl

# wb = openpyxl.Workbook()    # 新規作成
# wb.save("test.xlsx")        # test.xlsxで保存

wb = openpyxl.load_workbook("test.xlsx")    # 読み込み

all_sheets = wb.sheetnames
print(all_sheets)

ws = wb["Sheet"]
ws.title = 'シート1'
ws.sheet_properties.tabColor = "00FF00" # シートタブの色設定

wb.save("sample.xlsx")      # 別名で保存
```

> https://openpyxl.readthedocs.io/en/stable/worksheet_properties.html



#### cellの値の取得

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb["Sheet"]

a1 = ws["A1"]
print("A1=",a1.value)
```

- R1C1表記（行列表記）を使用する（同一の結果）

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb["Sheet"]

a1 = ws.cell(row=1, column=1)
print("A1=",a1.value)
```



| 記述          | 意味                  |
| ------------- | --------------------- |
| a1.value      | セルの値              |
| a1.coordinate | セルのアドレス → 'A1' |





#### cellへの値の代入

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb["Sheet"]

a1 = ws.cell(row=1, column=1)
a1.value = 'abc'
ws.cell(row=2,column=1, value='hehehe')
ws['A3'] = 'xyz'
wb.save("sample.xlsx")
```



#### cellの範囲

```python
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb["Sheet"]

a1 = ws.cell(row=1, column=1)
a1.value = 'abc'
ws['A2'] = 'xyz'

cell_range = ws["B1:B3"]	# tupleで返る
for cell, in cell_range: 
    print(cell.value)
```



【excel3.py】

```python
import openpyxl

# wb = openpyxl.Workbook()    # 新規作成
# wb.save("test.xlsx")        # test.xlsxで保存

wb = openpyxl.load_workbook("test.xlsx")    # 読み込み

all_sheets = wb.sheetnames
print(all_sheets)

ws = wb["Sheet"]
ws.title = 'シート1'
ws.sheet_properties.tabColor = "00FF00" # シートタブの色設定

value = 100
for row in ws["A1:B5"]:         # 通常の方法
    for cell in row:
        cell.value = value      # セルに書き込み
        value += 10

cell_range = ws["C1:C5"]
for cell, in cell_range:        # 1列しかない場合
    cell.value = 'x'

cell_range = ws["A10:E10"]
for cell in list(cell_range[0]):# 1行しかない場合
    cell.value = 'y'


wb.save("sample.xlsx")      # 別名で保存
```



#### 練習1

- 以下のプログラムを作成してください。【ren1.py】
  - data1.csvファイルの中身を読み込み、data1.xlsxを作成する
    - 1行目は項目を表す
  - csvは他のプログラムにより生成されるものとし、列数・行数は変動するものとする。
  - サンプルは2つ用意した
    - data1.csvからdata1.xlsxを作成する。
    - data2.csvからdata2.xlsxを作成する。





#### 練習2

- 以下のプログラムを作成してください。【ren2.py】
  - 指定したexcelのデータから、特定の範囲のデータをCSVとして保存する。
  - csvファイル名は、excelと同一とする。
    - 別サンプルとして、exdata1.xlsx,exdata2.xlsxも用意した。
  - 範囲はキーボードから入力し、指定するものとする。

【実行結果】

```
> python ren2.py
変換するexcelファイル名を入力してください：exdata1.xlsx
変換する範囲の開始は？：A3
変換する範囲の終了は？：C17
exdata1.csvを出力しました
```

