# 以快速排序例，计算将一个大小为1000的数组排序所需时间
# 使用Python随机生成多组长度递增的随机数列，使用不同的排序算法（如选择排序和归并排序）对这些数组排序，分析不同的
# 排序算法在不同长度数列下的运行效果
import random
import time


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


# 归并排序
list = []
# 更改数组规模
for i in range(1, 4):
    t = 0.0
# 进行1000次循环
    for j in range(1000):
        m = 0
        while m < 10**i:
            num = random.randint(0, 10000)
            if num not in list:
                m += 1
                list.append(num)
        start = time.time()
        MerSort(list, 0, len(list)-1)
        end = time.time()
        # print(list)
        t += end-start
        del list[:]
    print("{} 's time is {} s".format(10**i, t/1000))
