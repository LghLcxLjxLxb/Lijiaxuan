import random
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


list = []
n = int(input('请输入数组规模：'))
m = 0
while m < n:
    num = random.randint(0, 10000)
    if num not in list:
        m += 1
        list.append(num)
InsertSort(list)
print(list)
