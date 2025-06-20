# 基本テスト
# - 1つのファイルに対してwc.pyを実行し、行数、単語数、バイト数が正しいことを確認
# - 複数のファイルに対してwc.pyを実行し、各ファイルの行数、単語数、バイト数が正しいことを確認
# - 存在しないファイルに対してwc.pyを実行し、エラーメッセージが正しいことを確認

import pytest
import random
import shutil
import subprocess
import os
import sys

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
    "file_name, expected_lines, expected_words, expected_bytes",
    [
        ("wc_test_root/file_1.txt", 1, 4, 15),
        ("wc_test_root/file_multi1.txt", 6, 6, 31),
    ]
)
def test_wc_command_with_single_file(file_name, expected_lines, expected_words, expected_bytes):
    """Test wc command with a single file."""
    # make wc.py path by modulepath
    module_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(module_path, 'wc.py')
    result = subprocess.run(['python', filepath, file_name], capture_output=True, text=True)
    assert result.returncode == 0
    output = result.stdout.strip()
    lines, words, bytes_, filename = output.split()


@pytest.mark.parametrize(
    "file_names, expected_lines, expected_words, expected_bytes, expected_total_lines, expected_total_words, expected_total_bytes",
    [
        (["wc_test_root/file_0.txt", "wc_test_root/file_1.txt"], [1, 1], [4, 4], [15, 15], 2, 8, 30),
        (["wc_test_root/file_multi0.txt", "wc_test_root/file_multi1.txt"], [6, 6], [6, 6], [31, 31], 12, 12, 62),
        (["wc_test_root/file_0.txt", "wc_test_root/file_multi0.txt"], [1, 6], [4, 6], [15, 31], 7, 10, 46),
    ]
)
def test_wc_command_with_multiple_files(file_names, expected_lines, expected_words, expected_bytes, expected_total_lines, expected_total_words, expected_total_bytes):
    """Test wc command with multiple files."""
    # make wc.py path by modulepath
    module_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(module_path, 'wc.py')
    result = subprocess.run(['python', filepath] + file_names, capture_output=True, text=True)
    assert result.returncode == 0
    output = result.stdout.strip().splitlines()
    for i, line in enumerate(output[:-1]):
        lines, words, bytes_, filename = line.split()
        assert int(lines) == expected_lines[i]
        assert int(words) == expected_words[i]
        assert int(bytes_) == expected_bytes[i]
    total_line = output[-1].split()
    assert total_line[0] == str(expected_total_lines)
    assert total_line[1] == str(expected_total_words)
    assert total_line[2] == str(expected_total_bytes)

def test_wc_command_with_nonexistent_file():
    """Test wc command with a nonexistent file."""
    # make wc.py path by modulepath
    module_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(module_path, 'wc.py')
    result = subprocess.run(['python', filepath, 'nonexistent_file.txt'], capture_output=True, text=True)
    assert result.returncode != 0
    assert "No such file or directory" in result.stdout

def test_wc_command_with_directory():
    """Test wc command with a directory."""
    # make wc.py path by modulepath
    module_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(module_path, 'wc.py')
    result = subprocess.run(['python', filepath, 'wc_test_root'], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Is a directory" in result.stdout
