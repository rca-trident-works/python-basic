class RangeIterator:
    def __init__(self, start, end):
        self._current = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self._end:
            raise StopIteration
        current = self._current
        self._current += 1
        return current


# main
range_iter = RangeIterator(10, 15)
for number in range_iter:
    print(number)
