# Clone implementation of wc command
import os
import sys

def main():
    if len(sys.argv) < 2:
        # TODO: Print usage message
        sys.exit(1)

    lines_results = []
    words_results = []
    bytes_results = []
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"{file_path}: No such file or directory")
            continue
        num_lines, num_words, num_bytes = get_file_stats(file_path)
        lines_results.append(num_lines)
        words_results.append(num_words)
        bytes_results.append(num_bytes)

    print_results(file_paths, lines_results, words_results, bytes_results)

# Utils
def print_results(file_paths, lines_results, words_results, bytes_results):
    """Print the results in a formatted table."""
    item_count = len(file_paths)

    if item_count > 1:
        # 最終行に合計を追加
        total_lines = sum(lines_results)
        total_words = sum(words_results)
        total_bytes = sum(bytes_results)
        lines_results.append(total_lines)
        words_results.append(total_words)
        bytes_results.append(total_bytes)

        file_paths.append("total")

        # Adjust item count to include the total row
        item_count += 1

    lines_width = calculate_column_widths(lines_results)
    words_width = calculate_column_widths(words_results)
    bytes_width = calculate_column_widths(bytes_results)

    for i in range(item_count):
        print(f"{lines_results[i]:>{lines_width}} {words_results[i]:>{words_width}} {bytes_results[i]:>{bytes_width}} {file_paths[i]}")


def calculate_column_widths(array):
    """Calculate the width of each column based on the longest item in the array."""
    length = 0;
    max_length = max(len(str(item)) for item in array)
    if max_length <= 4:
        length = 4
    else:
        length = max_length

    return length + 1 # 1 is for the space between columns

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
