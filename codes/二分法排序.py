import random
import time


def binary_sort(list: list, reverse: bool = False):
    sorted_list = []
    for content in list:
        binary_insert(sorted_list, content, (0, sorted_list.__len__()))
    return sorted_list


def binary_insert(sorted_list: list, content, index_tuple: tuple):
    if index_tuple[0] == index_tuple[1]:
        return sorted_list.insert(index_tuple[0], content)

    middle_index = (index_tuple[0] + index_tuple[1]) // 2
    if sorted_list[middle_index] < content:
        binary_insert(sorted_list, content, (middle_index + 1, index_tuple[1]))
    else:
        binary_insert(sorted_list, content, (index_tuple[0], middle_index))


data = [random.randint(0, 100000) for i in range(100000)]
beforeT = time.clock()
print(binary_sort(data))
afterT = time.clock()
print(afterT - beforeT)
# print(binary_sort([
#     2,5,1,5,6,324,645,23,662,23,5,6,234,23,56,2312
# ]))
