# 将一个正整数分割成若干因子，求使因子乘积最大的正整数列
n = int(input('请输入一个整数：'))
if (n < 5):
    print(n)
a, b = divmod(n, 3)
if (b == 0):
    for i in range(a-1):
        print('3 × ', end='')
    print('3 = {}'.format(3**a))
elif (b == 1):
    for i in range(a-1):
        print('3 × ', end='')
    print('4 = {}'.format(3**(a-1)*4))
elif (b == 2):
    for i in range(a):
        print('3 × ', end='')
    print('2 = {}'.format(3**a*2))


# 1 如果n是2001，所求的正整数列是667个3相乘
# 2 原理：由规律可知，因为1本身是一个因子，而且乘以任何数都是数本身，所以应该尽量避免因子有1
#  数学归纳法可知，当因子本身是3，其次是2，可以得到最佳方案
