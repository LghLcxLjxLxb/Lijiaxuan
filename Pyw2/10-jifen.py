# 利用蒙特卡罗计算函数积分
import math
import random


def func(x):
    return x**2+4*x*math.sin(x)


def mengtekaluo(num):
    a = 2
    b = 3
    sum = 0
    for i in range(num):
        x = random.uniform(a, b)
        sum += func(x)
    print((b-a)/num*sum)


mengtekaluo(100000)
