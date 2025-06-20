import random


class RandomSequence:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        r_int = random.randint(1, 4)
        self.current += r_int
        return current


# main
random_seq = RandomSequence(1)
for _ in range(10):
    print(next(random_seq))
