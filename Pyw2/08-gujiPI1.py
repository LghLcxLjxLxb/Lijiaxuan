# 估计π值的第一种方法：布冯-拉普拉斯方法
import random
import numpy as np

# 在一个正方形区域内投针，计算投在圆区域内的针的数量，然后由其比例得到估计值


def Throwneedles(numneedles):
    Incircle = 0
    for i in range(numneedles):
        x = random.random()
        y = random.random()
        if ((x*x+y*y) <= 1):
            Incircle += 1
    return 4*Incircle/numneedles

# 进行多次实验，计算每次实验后得到的估计值的均值和标准差，并将最后的结果输出


def getEst(numneedles, numtrails):
    estimates = []
    for t in range(numtrails):
        estimates.append(Throwneedles(numneedles))
    stDev = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est = %s ,' % (str(round(curEst, 10))),
          'Stdev = %s ,' % (str(round(stDev, 5))),
          'Numneedles = %d ,' % numneedles)
    return curEst, stDev

# 给定精度，测试多次


def Est(precision, numtrails):
    numneedles = 1000
    stDev = precision
    while stDev > precision/1.96:
        (curEst, stDev) = getEst(numneedles, numtrails)
        numneedles *= 2


Est(0.01, 100)
