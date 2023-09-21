# 算数表达式
a = int(input('请输入一个数： '))
b = a**(1/3)
print(b)
# 近似算法


def jinsi(num):
    if (num < 0):
        temp = -num
    else:
        temp = num
    pre = 0.0001
    high = temp/2
    while abs(high**3-temp) > pre:
        if high**3 > temp:
            high = high-high/2
        else:
            high = high+high/2
    return high


num = float(input())
if (num > 0):
    print(jinsi(num))
else:
    print(-jinsi(num))
