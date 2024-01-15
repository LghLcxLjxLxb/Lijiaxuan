# 求两个正整数的最大公约数
# a = int(input('请输入第一个正整数：'))
# b = int(input('请输入第二个正整数：'))
# for i in range(2,min(a,b)+1):
#   if(a%i==0 and b%i==0):
#     max = i
# print(max)


# 辗转相除求最大公约数
a = int(input('请输入第一个正整数：'))
b = int(input('请输入第二个正整数：'))
temp1 = min(a, b)
temp2 = max(a, b)
mod = temp2 % temp1
while mod != 0:
    temp2 = temp1
    temp1 = mod
    mod = temp2 % temp1
print(temp1)
