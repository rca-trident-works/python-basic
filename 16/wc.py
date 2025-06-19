# Clone implementation of wc command

def main():
    pass

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
