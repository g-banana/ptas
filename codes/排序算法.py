import random
# import time
#
#
# def binary_sort(list: list, reverse: bool = False):
#     sorted_list = []
#     for content in list:
#         binary_insert(sorted_list, content, (0, sorted_list.__len__()))
#     return sorted_list
#
#
# def binary_insert(sorted_list: list, content, index_tuple: tuple):
#     if index_tuple[0] == index_tuple[1]:
#         return sorted_list.insert(index_tuple[0], content)
#
#     middle_index = (index_tuple[0] + index_tuple[1]) // 2
#     if sorted_list[middle_index] < content:
#         binary_insert(sorted_list, content, (middle_index + 1, index_tuple[1]))
#     else:
#         binary_insert(sorted_list, content, (index_tuple[0], middle_index))
#
#
# data = [random.randint(0, 100000) for i in range(100000)]
# beforeT = time.clock()
# print(binary_sort(data))
# afterT = time.clock()
# print(afterT - beforeT)
# # print(binary_sort([
# #     2,5,1,5,6,324,645,23,662,23,5,6,234,23,56,2312
# # ]))


# # 二分法查找
# def binary_search(list,item):
#     low = 0
#     heigh = len(list) - 1
#
#     while(low <=  heigh):
#         mid = (low + heigh) // 2
#         if list[mid] < item:
#             low = mid + 1
#         if list[mid] > item:
#             heigh = mid - 1
#         if list[mid] == item:
#             return mid
#
#     return False
#
# if __name__ == '__main__':
#     list = [ i for i in range(10) ]
#     index = binary_search(list,9)
#     print(index)

# # 冒泡排序
# def bubble_sort(list):
#     length = len(list)
#     for i in range(length):
#         for j in range(length-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#
# if __name__ == '__main__':
#     list = [random.randint(1,100) for i in range(20)]
#     print(list)
#     bubble_sort(list)
#     print(list)


# # 选择排序
# def select_sort(list):
#     def pick_min(sublsit):
#         min_index = 0
#         for i in range(1,len(sublsit)):
#             if sublsit[i] < sublsit[min_index]:
#                 min_index = i
#         return min_index
#     sorted_list = []
#     length = len(list)
#     for i in range(length):
#         sorted_list.append(list.pop(pick_min(list)))
#     return sorted_list
# if __name__ == '__main__':
#     list = [random.randint(1,100) for i in range(20)]
#     print(list)
#     sorted_list = select_sort(list)
#     print(sorted_list)

#冒泡算法比较的同时还存在交换操作，选择算法只需比较但是消耗了额外一倍空间来存放生成的新数组。应是后者空间换时间（不过时空复杂度均相等）


#https://blog.csdn.net/weixin_41966991/article/details/81808636
# 传统快速排序(不稳定)三种写法见 https://baike.baidu.com/item/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95
# 快排分而治之(D&C)的实现 https://baike.baidu.com/item/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95
# 单边写法
# def quick_sort(list,l,r):
#     if not l < r:
#         return
#     key = list[r]
#     i = l - 1
#     for j in range(l,r):
#         if list[j] < key:
#             i += 1
#             list[i],list[j] = list[j], list[i]
#     i += 1
#     list[i], list[r] = list[r], list[i]
#     quick_sort(list,l,i-1)
#     quick_sort(list,i+1,r)

# # 双边写法
# def quick_sort(list,left,right):
#     if not left < right:
#         return
#     key = list[left]
#     i = left
#     j = right
#     while(i < j):
#         while(i < j and list[j] > key):
#             j -= 1
#         if i < j:
#             list[i] = list[j]
#             i += 1
#         while(i < j and list[i] < key):
#             i += 1
#         if i < j:
#             list[j] = list[i]
#             j -= 1
#     list[i] = key
#     quick_sort(list,left,i-1)
#     quick_sort(list,i+1,right)
#
# if __name__ == '__main__':
#     list = [random.randint(1,100) for i in range(5)]
#     print(list,)
#     quick_sort(list,0,len(list)-1)
#     print(list)


# # 稳定的快速排序（最简单但性能不好）
# def quick_sort(list):
#     if len(list) < 2:
#         return list
#     mid_val = list[0]
#     lower_part = []
#     heighter_part = []
#     for it in list[1:]:
#         if it <= mid_val:
#             lower_part.append(it)
#         else:
#             heighter_part.append(it)
#
#     lower_part = quick_sort(lower_part)
#     heighter_part = quick_sort(heighter_part)
#     return lower_part + [mid_val] + heighter_part
#
# if __name__ == '__main__':
#     list = [random.randint(0,100) for i in range(20)]
#     sorted_list = quick_sort(list)
#     print(sorted_list)

# 第二种快排构造队列来生成新数组,空间复杂度O(n^2)，有点事最易理解写出并且具备稳定性，空间复杂度更小且同样具备稳定性的快排见 https://www.docin.com/p-1668725740.html

# # 快速排序优化拓展(多值取中)
# def quick_sort(list,lef,rig):
#     mid_ind = partion(list,lef,rig)
#     if mid_ind != -1:
#         quick_sort(list,lef,mid_ind-1)
#         quick_sort(list,mid_ind+1,rig)
#
# def partion(list,lef,rig):
#     if not lef < rig:
#         return -1
#     pickaxis(list,lef,rig)
#     axis = list[lef]
#     while lef < rig:
#         while lef < rig and list[rig] > axis:
#             rig -= 1
#         if lef < rig:
#             list[lef] = list[rig]
#             lef += 1
#         while lef < rig and list[lef] < axis:
#             lef += 1
#         if lef < rig:
#             list[rig] = list[lef]
#             rig -= 1
#
#     list[lef] = axis
#     return lef
#
# def pickaxis(list,lef,rig):
#     if (rig-lef) < 2:
#         return
#     mid = lef + (rig - lef)//2
#     if (list[mid] < list[lef] and list[mid] > list[rig]) or (list[mid] > list[lef] and list[mid] < list[rig]):
#         list[lef],list[mid] = list[mid],list[lef]
#     if (list[rig] < list[mid]) and (list[rig] > list[lef]) or (list[rig] > list[mid]) and (list[rig] < list[lef]):
#         list[lef],list[rig] = list[rig],list[lef]
#
#
# if __name__ == '__main__':
#     list = [random.randint(0,100) for i in range(20)]
#     quick_sort(list,0,len(list)-1)
#     print(list)

# 归并排序
def merge(list, lef, mid, rig, temp):
    l = list[lef:mid+1]
    r = list[mid+1:rig+1]
    for i in range(len(l)+len(r)):
        if not(l and r):
            break
        if l[0] < r[0]:
            temp.append(l.pop(0))
        else:
            temp.append(r.pop(0))

    temp.extend(l)
    temp.extend(r)
    # print(temp)
    list[lef:rig+1] = temp
    temp.clear()

def merger_sort(list, lef, rig, temp):
    if rig > lef:
        mid = lef + (rig-lef)//2
        merger_sort(list, lef, mid, temp)
        merger_sort(list, mid + 1, rig, temp)
        merge(list, lef, mid, rig, temp)

if __name__ == '__main__':
    list = [random.randint(0,100) for i in range(20)]
    temp = []
    merger_sort(list, 0, len(list) - 1, temp)
    print(temp)
    print(list)

