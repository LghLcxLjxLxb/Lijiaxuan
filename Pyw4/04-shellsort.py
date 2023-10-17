# 希尔排序
def shellsort(arr):
    length = len(arr)
    gap = int(length/2)
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and arr[j] < arr[j-gap]:
                temp = arr[j]
                arr[j] = arr[j-gap]
                arr[j-gap] = temp
                j -= gap
        gap = int(gap/2)


list = []
n = int(input('请输入数组规模：'))
for i in range(n):
    list.append(int(input()))
shellsort(list)
print(list)
# 时间复杂度：
# 采用gap=gap/2的迭代方法
# 第一次比较：有n/2组，每组2个元素，最坏时间为1*n/2;
# 第二次比较：有n/4组，每组4个元素，最坏时间为（1+2+3）*n/4;
# 第三次比较：有n/8组，每组8个元素，最坏时间为（1+2+3+4+5+6+7）*n/8;
# ...
# 得出规律：最终的最坏时间为1*n/2+（1+2+3）*n/4+（1+2+3+4+5+6+7）*n/8+...=O（n*lgn）
# 空间复杂度：O（1），希尔排序和直接插入排序相同，都是原址重排，不需要额外空间存储
