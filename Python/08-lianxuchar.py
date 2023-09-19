str = input('请输入一串字符串')
i = 0
for i in range(len(str)-1):
    if (str[i] == str[i+1]):
        break
if (i < len(str)-2 or str[len(str)-1] == str[len(str)-2]):
    print('Yes')
else:
    print('No')
