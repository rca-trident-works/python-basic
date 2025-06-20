class FileIterator:
    def __init__(self, file_path):
        self._file = open(file_path, "r", encoding="utf8")

    def __iter__(self):
        return self

    def __next__(self):
        _line = self._file.readline()
        if not _line:
            self._file.close()
            raise StopIteration
        return _line.strip()

    def __del__(self):
        if hasattr(self, "_file"):
            self._file.close()


# main
file_iter = FileIterator("sample.txt")
for line in file_iter:
    print(line.strip())
