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
    input_paths = sys.argv[1:]

    file_paths = []

    # Collect file paths from command line arguments
    for i, path in enumerate(input_paths):
        if not os.path.exists(path):
            print(f"{path}: No such file or directory")
            continue
        elif os.path.isdir(path):
            print(f"{path}: Is a directory (Currently not supported)")
            continue
        elif not os.path.isfile(path):
            print(f"{path}: Not a regular file (Currently not supported)")
            continue
        else:
            file_paths.append(path)

    for file_path in file_paths:
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
        for array in (lines_results, words_results, bytes_results):
            array.append(sum(array))
        file_paths.append("total")
        # Adjust item count to include the total row
        item_count += 1

    lines_width = get_max_width(lines_results)
    words_width = get_max_width(words_results)
    bytes_width = get_max_width(bytes_results)

    max_width = max(lines_width, words_width, bytes_width)

    lines_width = max(max_width, lines_width + 1)
    words_width = max_width
    bytes_width = max_width

    for i in range(item_count):
        print(f"{lines_results[i]:>{lines_width}} {words_results[i]:>{words_width}} {bytes_results[i]:>{bytes_width}} {file_paths[i]}")

def get_max_width(array):
    """Calculate the width of each column based on the longest item in the array."""
    return max(len(str(item)) for item in array)

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
