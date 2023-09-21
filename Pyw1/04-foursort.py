import numpy as np
num = [1,2,3,4]
for i in range(4):
  print('请输入第{}个数： '.format(i+1),end='')
  num[i] = int(input(''))
num = sorted(num,reverse=True)
print(num)