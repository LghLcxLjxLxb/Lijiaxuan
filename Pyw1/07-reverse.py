# 用for循环实现倒排序输出
str = input('请输入一串字符: ').strip('[]')
str = str.split(',')
num = [int(x) for x in str]
print('[', end='')
for i in range(len(num)-1, 0, -1):
    print(num[i], end=',')
print(num[0], end=']')


# 用while循环实现倒排序输出
str = input('请输入一串字符: ').strip('[]')
str = str.split(',')
num = [int(x) for x in str]
print('[', end='')
i = len(num)-1
while i > 0:
    print(num[i], end=',')
    i -= 1
print(num[0], end=']')
