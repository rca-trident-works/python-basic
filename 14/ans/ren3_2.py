# zip を使用した例
def pair_sum(iter1, iter2):
    for x, y in zip(iter1, iter2):
        yield x + y


# zip を使用しない例
# def pair_sum(iter1, iter2):
#     i = 0
#     while i < len(iter1) and i < len(iter2):
#         yield iter1[i] + iter2[i]
#         i += 1


list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
for sum_val in pair_sum(list1, list2):
    print(sum_val)
