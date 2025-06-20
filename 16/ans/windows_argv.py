import sys


def sys_argv():
    """
    Windowsのコマンドライン引数を取得するための関数。
    ワイルドカードを含む引数を展開してsys.argvに設定する。
    """
    if not sys.platform.startswith("win"):
        return

    import glob

    temp_list = []
    for path in sys.argv:
        if "*" in path or "?" in path:
            glob_list = glob.glob(path)
            if glob_list:
                # ワイルドカードに合致するファイルリスト
                temp_list += [filename for filename in glob_list]
            else:
                # ワイルドカードで一致するものがない場合
                temp_list += [path]
        else:
            # 通常の引数
            temp_list += [path]

    sys.argv = temp_list


if __name__ == "__main__":
    # Windows環境でのコマンドライン引数を取得
    sys_argv()
    print(sys.argv)
