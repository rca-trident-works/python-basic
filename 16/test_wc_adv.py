# 拡張テスト
# - wc.pyの出力とシステムのwcコマンドの出力を比較する

import pytest
import random
import shutil
import subprocess
import os
import sys
import glob

def setup_test_environment():
    # テストに使うディレクトリとファイルを作成
    if not os.path.exists('wc_test_root'):
        os.makedirs('wc_test_root')

        # ディレクトリ内にいくつかのファイルを作成
        for i in range(5):
            with open(f'wc_test_root/file_{i}.txt', 'w') as f:
                f.write(f'This is file {i}\n')
        for i in range(3):
            with open(f'wc_test_root/file_multi{i}.txt', 'w') as f:
                f.write(f'This\nfile\nhas\nmultiple\nlines\n{i}\n')

def teardown_test_environment():
    # テスト後に作成したディレクトリとファイルを削除
    if os.path.exists('wc_test_root'):
        shutil.rmtree('wc_test_root')

@pytest.fixture(scope='module', autouse=True)
def manage_test_environment():
    setup_test_environment()
    yield
    teardown_test_environment()

@pytest.mark.parametrize(
    "file_names",
    [
        ["wc_test_root/file_0.txt"],
        ["wc_test_root/file_0.txt", "wc_test_root/file_1.txt"],
        ["wc_test_root/file_multi0.txt", "wc_test_root/file_multi1.txt"],
        ["wc_test_root/file_0.txt", "wc_test_root/file_multi0.txt"],
        # TODO: Replace with wildcard patterns?
        ["wc_test_root/file_0.txt", "wc_test_root/file_1.txt", "wc_test_root/file_3.txt", "wc_test_root/file_4.txt", "wc_test_root/file_multi0.txt", "wc_test_root/file_multi1.txt", "wc_test_root/file_multi2.txt"],
    ]
)
def test_compare_wc_command(file_names):
    """Compare the output of wc.py with the system wc command."""
    module_path = os.path.dirname(os.path.abspath(__file__))
    wc_py_path = os.path.join(module_path, 'wc.py')
    # Expand wildcards if necessary
    expanded_files = []
    for file_name in file_names:
        if '*' in file_name:
            expanded_files.extend(glob.glob(os.path.join('wc_test_root', file_name)))
        else:
            expanded_files.append(file_name)

    print(f"Testing with files: {expanded_files}")
    # Run the custom wc.py script
    result_py = subprocess.run(['python', wc_py_path] + expanded_files, capture_output=True, text=True)
    # Run the system wc command
    result_sys = subprocess.run(['wc'] + expanded_files, capture_output=True, text=True)
    assert result_py.returncode == 0
    assert result_sys.returncode == 0
    # Compare outputs line by line
    py_lines = result_py.stdout.strip().split('\n')
    sys_lines = result_sys.stdout.strip().split('\n')
    for py_line, sys_line in zip(py_lines, sys_lines):
        assert py_line.strip() == sys_line.strip()
