class FileIterator:
    def __init__(self, file_path):
        self._file = open(file_path, 'r', encoding='utf8')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            _line = self._file.readline()
            # if len(line) == 0:   # EOFの時の処理
            if not _line:   # EOFの時の処理
                raise StopIteration
        except StopIteration:
            self._file.close()
            raise StopIteration
        return _line


# main
file_iter = FileIterator("sample.txt")
for line in file_iter:
    print(line.strip())
