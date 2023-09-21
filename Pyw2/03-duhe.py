# A，B岸上分别存在的物种
A = [['狼', 1], ['羊', 1], ['菜', 1]]
B = [['狼', 0], ['羊', 0], ['菜', 0]]
size = len(A)
# 记录最近一次渡河的物种
number = -1
# 程序所需的步骤数
count = -1

# 判断A或B岸上的生物是否共存


def judge(A):
    if (A[1][1] == 1 and A[0][1]+A[2][1] == 1):
        return False
    else:
        return True

# 将生物从A岸运到B岸


def A_to_B():
    global number
    global count
    for i in range(size):
        if (A[i][1] == 1) and i != number:
            A[i][1] -= 1
            if judge(A):
                B[i][1] += 1
                number = i
                count += 1
                print("%s ,A->B" % A[i][0])
                break
            else:
                A[i][1] += 1
                continue
        else:
            continue

# 将生物从B岸运到A岸


def B_to_A():
    global number
    global count
    if judge(B) == False:
        for j in range(size):
            if B[j][1] == 1 and j != number:
                B[j][1] -= 1
                A[j][1] += 1
                count += 1
                number = j
                print("%s ,B->A" % B[j][0])
                break
            else:
                continue
    else:
        if B[0][1]+B[1][1]+B[2][1] == 3:
            print('任务完成')
        else:
            print('B->A')

# 将岸上的所有生物制作列表


def shore(A):
    list1 = []
    for i in range(size):
        if (A[i][1] == 1):
            list1.append(A[i][0])
    return list1

# 判断是否成功


def success():
    if (B[0][1]+B[1][1]+B[2][1] == 3):
        return True
    else:
        return False


# 循环输出步骤
while 1:
    print('A岸上有', shore(A))
    print('B岸上有', shore(B))
    A_to_B()
    print('A岸上有', shore(A))
    print('B岸上有', shore(B))
    B_to_A()
    if success():
        print('总共需要 %d 步' % count)
        break
