class Counter:
    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count

# main 
counter = Counter(0)
for _ in range(5):
    print(next(counter))
