# 用while循环实现笨方法求解根号2，一旦找到所要的g就跳出循环
def Sqrt_two():
    c = 2
    i = 0
    g = 0
    for g in range(0, c+1):
        if (g*g > c):
            break
    g -= 1
    while 1:
        if (abs(g*g-c) > 0.0001):
            g += 0.00001
            i += 1
            print('%d:g = %.5f' % (i, g))
        else:
            break


Sqrt_two()
