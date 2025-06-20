class FileIterator:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf8") as self.file:
            self.lines = self.file.readlines()
        # self.file = open(file_path, 'r', encoding='utf8')
        # self.lines = self.file.readlines()
        # self.file.close()
        self._index = 0 

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.lines):
            raise StopIteration
        current = self.lines[self._index]
        self._index += 1
        return current


# main
file_iter = FileIterator("sample.txt")
for line in file_iter:
    print(line.strip())
