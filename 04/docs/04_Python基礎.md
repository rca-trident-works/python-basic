# 04 Python基礎

## 気楽な入門編2

### リストについて

- データをひとまとめにした配列のような複合データ構造
  【list_0.py】

  ```python
  int_list = [1, 2, 3, 4, 5]
  float_list = [1.0, 2.0, 3.0, 4.0, 5.0]
  mix_list = [1, 2.0, 'abc', [3, 4], [5.0, 6.0, 7.0]]
  ```

- 添字（インデックス）を使用して、取り出し＆操作が可能

  - スライスも利用可能
    ```python
    mix_list[1]		# 2.0
    mix_list[2][1]  # 'b'
    mix_list[4][0]  # 5.0
    mix_list[3:]    # [[3, 4], [5.0, 6.0, 7.0]]
    mix_list[2:4]   # ['abc', [3, 4]]
    ```




#### 変数の扱い（重要）

- 整数・浮動小数点はミュータブル（mutable）
- リストはミュータブル（mutable）
- 文字列自体はイミュータブル（immutable）
  - 文字列変数は、ミュータブル（mutable）



### 練習1

(1) 以下のリストを定義し、目的のデータを取り出してください。
【list_1.py】

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

- 40〜60までの要素の合計

- データの個数

- 最後の3個のデータの平均

- 最大値と最小値の差

- 60,70,80 を 5,4,3 に置き換える

  

(2) 以下の動作を確認してください。
【list_2.py】

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num2 = [1, 2, numbers, 3, 4]
```

- numbers , num2 にどのような値が格納されているか確認してください。
- numbers の値を変更してください。
  例） 60 → 0
  - その後、numbers , num2 にどのような値が格納されているか確認してください。
- なぜ、このようなことが起きるか、考えてください。



### プログラミング、はじめの一歩

- サンプルを実行してみよう
  【Fibonacci.py】

  ```python
  # フィボナッチ級数
  # 2項の和により次項が定まる
  a, b = 0, 1
  while a < 10:
      print(a)
      a, b = b, a+b
  ```

- `print()`関数について調べてください。

  - キーワード引数とは何ですか？

    ```python
    print(a, end=',')
    ```

    という記述は、どのような動作をするかよく読んでください。



### 調査

- markdown記法について、調査＆確認してください。

  - markdownを記述するためのツールを決めてください。
    - vscode
    - typora （有料）
    - obsidian
    - Boostnote
    - Joplin
    - Zettlr
    - Haroopad
    - MarkText
    - GhostWriter
    - StackEdit




- python のコード記述ガイドライン（コーディングスタイル） PEP8について調べ、まとめてください。
マークダウン記法で書いてください。【pep8.md】



#### vscodeの場合

- 良さそうなプラグイン
  - Markdown All in One
  - Markdown Preview Enhanced



#### Obsidianの場合

- 使っているコミニュティプラグイン

<img src="./04_Python基礎_解答付.assets/image-20250412225601143.png" alt="image-20250412225601143" style="zoom:33%;" />



#### typoraの場合

- ほぼすべての機能を網羅している

  - 外部拡張機能 mermaid 記法を学ぶと良い

    > https://mermaid.js.org/intro/



