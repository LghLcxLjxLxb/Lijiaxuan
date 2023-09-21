num = [1,2,3]
for i in range(3):
  print('请输入第{}个数: '.format(i+1),end='')
  num[i]=int(input(''))
max_num=max(num[0],num[1],num[2])
min_num=min(num[0],num[1],num[2])
print(max_num,end='')
for i in range(3):
  if(num[i]!=max_num and num[i]!=min_num):
    print(' ',num[i],end='')
    break
print(' ',min_num,end='')