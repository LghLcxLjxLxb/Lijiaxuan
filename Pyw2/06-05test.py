# 用牛顿法求解根号2的程序中，把g的初始值设为c或c/4等，对结果有影响吗
def Newton_Sqrt(c):
    g = c/4
    i = 0
    while (abs(g*g-c) > 0.00000000001):
        i += 1
        g = (g+c/g)/2
        print("%d:g = %.13f" % (i, g))


n = int(input())
Newton_Sqrt(n)

"""当g=c/2时，结果为
    1:g = 1.5000000000000
    2:g = 1.4166666666667
    3:g = 1.4142156862745
    4:g = 1.4142135623747
   当g=c时，结果为
    1:g = 1.5000000000000
    2:g = 1.4166666666667
    3:g = 1.4142156862745
    4:g = 1.4142135623747
   当g=c/4时，结果为
    1:g = 2.2500000000000
    2:g = 1.5694444444444
    3:g = 1.4218903638151
    4:g = 1.4142342859401
    5:g = 1.4142135625249
    6:g = 1.4142135623747
"""
# 由以上实验可知，改变g的初始值后对求解根号2没有影响
