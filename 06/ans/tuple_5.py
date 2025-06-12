# タプルの方がメモリ使用量が少ない
import sys

list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))

print(f"リストのサイズ: {list_size} bytes")
print(f"タプルのサイズ: {tuple_size} bytes")
