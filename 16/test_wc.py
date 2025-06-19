import pytest
import random
import shutil
import os

def setup_test_environment():
    # テストに使うディレクトリとファイルを作成
    
    # rootディレクトリ作成
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
    "file_name, expected_output",
    [
        ("wc_test_root/file_0.txt", "1 5 23 wc_test_root/file_0.txt"),
        ("wc_test_root/file_multi0.txt", "6 30 150 wc_test_root/file_multi0.txt"),
    ]
)
def test_wc_command_with_single_file(file_name, expected_output):
    pass


