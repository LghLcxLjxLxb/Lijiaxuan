import math


def func(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            break
    if (i >= int(math.sqrt(n)) and n % i != 0):
        print('{}是质数'.format(n))
    else:
        print('{}不是质数'.format(n))


a = int(input('请输入一个整数：'))
func(a)
