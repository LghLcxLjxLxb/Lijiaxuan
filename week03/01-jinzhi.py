# 通过使用`int()`函数或`math.floor()`函数可以取得一个数的整数部分，
# 使用取模运算符或`math.modf()`函数可以获得一个数的小数部分。
n = float(input('请输入一个十进制小数：'))
# 取整数部分
integer = int(n)
# 取小数部分
decimal = n % 1
# 存放整数部分和小数部分的二进制
integers = []
decimals = []
# 辗转相除法求整数部分的二进制
div, mod = divmod(integer, 2)
while div != 0:
    integers.insert(0, mod)
    div, mod = divmod(div, 2)
if (mod == 1):
    integers.insert(0, mod)
# 辗转相乘求小数部分的二进制
amass = decimal*2
while amass % 1 != 0.0:
    decimals.append(int(amass))
    if (int(amass) == 1):
        amass -= 1
    amass *= 2
decimals.append(1)
print('{}的二进制形式为：'.format(n), end='')
for i in range(len(integers)):
    print(integers[i], end='')
print('.', end='')
for i in range(len(decimals)):
    print(decimals[i], end='')
