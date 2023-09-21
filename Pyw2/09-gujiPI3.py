# 利用梅钦公式计算圆周率
import math


def machin_of_pi():
    pi = 4*(4*math.atan(1/5)-math.atan(1/239))
    print('%.10f' % pi)
    return


machin_of_pi()
