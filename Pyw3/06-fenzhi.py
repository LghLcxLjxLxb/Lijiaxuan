store = int(input('请输入一个你的分数：'))
if store<60 :
  print('不及格')
elif store>=60 and store<=74:
  print('及格')
elif store>=75 and store<=89:
  print('良好')
elif store>=90:
  print('优秀')