# 估计PI值的第二种方法--无穷级数
def Guess_PI(error):
    a = 1
    b = 1
    sum = 0
    while 1/b > error:
        if a % 2 != 0:
            sum += 1/b
        else:
            sum -= 1/b
        a += 1
        b += 2
    print('%.10f' % (4*sum))
    return


Guess_PI(0.0001)
