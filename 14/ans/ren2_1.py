class Counter:
    def __init__(self, start):
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self._current
        self._current += 1
        return current


# main
counter = Counter(0)
for _ in range(5):
    print(next(counter))
