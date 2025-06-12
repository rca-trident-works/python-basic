# 01 Python実行環境の準備

[TOC]

---

# 授業前アンケート

https://forms.gle/zVhYx83qyRAdQSW19



## Pythonの環境

様々な方法がある。

### (Vanilla) Python

- 素のPython環境
- エディタでプログラム作成
- CUIで実行

#### 仮想環境作成に別途ツールが必要

- venv
- pyenv
- poetry



### Anaconda

- 各バージョンのPythonを管理可能

- 科学計算のための自由なオープンソースディストリビューション

- パッケージ管理とデプロイメントを簡略化することを狙ったもの

  > [Wikipedia](https://ja.wikipedia.org/wiki/Anaconda_(Python%E3%83%87%E3%82%A3%E3%82%B9%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3))

#### 同梱のツール

- conda



### Jupyter Notebook

- インタラクティブなGUI実行環境(ブラウザ上で)
- 仮想環境が利用可能
  - 異なるバージョンのpythonも利用可能
  - モジュールの管理が用意
- ライブラリがインストール済み



### IDEの利用

- Spider
- IDLE
- JupyterLab
- PyCharm
- vscode



## 実際の手順

### Windows Terminalの設定

- Terminalの初期設定がPower Shellになっている→コマンドプロンプトに変更

<img src="./01_1_Python実行環境の準備.assets/image-20250408100842199.png" alt="image-20250408100842199" style="zoom:50%;" />

<img src="./01_1_Python実行環境の準備.assets/image-20250408101054715.png" alt="image-20250408101054715" style="zoom: 33%;" />



### エディタ環境 ダウンロード

- microsoft vscode
  - https://code.visualstudio.com/download
  - User Installer 64bit を使用する

<img src="./01_1_Python実行環境の準備.assets/image-20250408095449342.png" alt="image-20250408095449342" style="zoom:33%;" />

- System Installerでも問題はないが、Windows自体の動作に影響を与えるので要注意
  - マルチユーザで利用するマシンの場合、他のユーザでもvscodeが利用できてしまう



#### 必須設定プラグイン

- Japanese Language Pack for Visual Studio Code
- Python
- Git Graph

#### おすすめプラグイン

- indent-rainbow

  




### バージョン管理（git）のダウンロード

- git を使用
  - https://gitforwindows.org/

<img src="./01_1_Python実行環境の準備.assets/image-20250408095726873.png" alt="image-20250408095726873" style="zoom: 33%;" />



#### gitのインストール

- ダウンロードしたファイルの実行
- 注意すべき箇所1
  - default editor を 「Visual Studio Code」にする

<img src="./01_1_Python実行環境の準備.assets/image-20250408100203438.png" style="zoom: 50%;" />



- 注意すべき箇所2

<img src="./01_1_Python実行環境の準備.assets/image-20250408100317477.png" style="zoom:50%;" />

#### 必須設定

- Terminalを開く
- 名前にスペースが含まれない場合は「"」は省略可
- 初期のブランチ名を「main」に設定する
  - 少し前までは「master」で固定（というルール）されていた。
    世界の言葉に対する反応への対応。

> https://phoeducation.work/entry/20210720/1626735480

```
C:\Users\satoshi>git config --global user.name "自分の名前"
C:\Users\satoshi>git config --global user.email 自分のEメールアドレス
```

- 先の「Override the default branch name for new repositories」（注意すべき箇所2）を選択しなかった場合手動で設定

```
C:\Users\satoshi>git config --global init.defaultBranch main
```



### 3) Anacondaのダウンロード

- 授業ではAnacondaを利用して、インストール＆実行環境の用意をする。
  - 以下のどちらかからダウンロードする（どちらも同じもの）



https://www.anaconda.com/download

<img src="./01_1_Python実行環境の準備.assets/image-20250408102031308.png" alt="image-20250408102031308" style="zoom:33%;" />

- バージョンは、3.12　64-bit版(912.3MB)



#### ダウンロードしたファイルを実行

- Anaconda3-2024.02-1-Windows-x86_64.exe
- 注意すべき選択箇所

<img src="./01_1_Python実行環境の準備.assets/image-20250408102617635.png" alt="image-20250408102617635" style="zoom: 50%;" />







