# 使用Python随机生成多组长度递增的随机数列，使用不同的排序算法（如选择排序和归并排序）对这些数组排序，分析不同的
# 排序算法在不同长度数列下的运行效果
import random


def Merge(list, begin, mid, end):
    sublist = []
    i = begin
    j = mid+1
    while i <= mid and j <= end:
        if list[i] < list[j]:
            sublist.append(list[i])
            i += 1
        else:
            sublist.append(list[j])
            j += 1
    while i > mid and j <= end:
        sublist.append(list[j])
        j += 1
    while i <= mid and j > end:
        sublist.append(list[i])
        i += 1
    k = begin
    for i in range(len(sublist)):
        list[k] = sublist[i]
        k += 1
    return
# 归并排序


def MerSort(list, begin, end):
    if (begin >= end):
        return
    else:
        mid = int((begin+end)/2)
        MerSort(list, begin, mid)
        MerSort(list, mid+1, end)
        Merge(list, begin, mid, end)
        return
# 快速排序


def QuickSort(list, begin, end):
    if begin < end:
        key = list[end]
        i = begin
        for j in range(begin, end):
            if (list[j] <= key):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i += 1
        temp = list[i]
        list[i] = list[end]
        list[end] = temp
        QuickSort(list, begin, i-1)
        QuickSort(list, i+1, end)
    else:
        return
# 选择排序


def Select(list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if (list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return
# 插入排序


def InsertSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while list[j] > key and j >= 0:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return


# 归并排序
list = []
for i in range(2, 4):
    m = 0
    while m < 10**i:
        num = random.randint(0, 10000)
        if num not in list:
            m += 1
            list.append(num)
    MerSort(list, 0, len(list)-1)
    print(list)
    print('\n')
    del list[:]

# 插入排序
list = []
for i in range(2, 4):
    m = 0
    while m < 10**i:
        num = random.randint(0, 10000)
        if num not in list:
            m += 1
            list.append(num)
    InsertSort(list)
    print(list)
    print('\n')
    del list[:]


# 选择排序
list = []
for i in range(2, 4):
    m = 0
    while m < 10**i:
        num = random.randint(0, 10000)
        if num not in list:
            m += 1
            list.append(num)
    Select(list)
    print(list)
    print('\n')
    del list[:]


# 快速排序
list = []
for i in range(2, 4):
    m = 0
    while m < 10**i:
        num = random.randint(0, 10000)
        if num not in list:
            m += 1
            list.append(num)
    Select(list)
    print(list)
    print('\n')
    del list[:]


# 以上列出数随机数组的归并排序，选择排序，插入排序和快速排序方法，归并排序和快速排序的速度相对较快，而插入排序和选择排序相对较慢
