# Clone implementation of wc command
import os
import sys

def main():
    if len(sys.argv) < 2:
        # TODO: Print usage message
        sys.exit(1)

    # 単ファイル, 複数ファイル指定に対応
    total_lines = 0
    total_words = 0
    tital_bytes = 0
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"{file_path}: No such file or directory")
            continue
        num_lines, num_words, num_bytes = get_file_stats(file_path)
        # 2個以上ならtotalを集計
        if len(file_paths) > 1:
            total_lines += num_lines
            total_words += num_words
            tital_bytes += num_bytes

        # print(f"{num_lines:>5} {num_words:>5} {num_bytes:>5} {file_path}")

def get_file_stats(file_path):
    """Get the number of lines, words, and bytes in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_bytes = len(content.encode('utf-8'))
        return num_lines, num_words, num_bytes
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, 0, 0

if __name__ == "__main__":
    main()
