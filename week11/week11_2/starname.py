from github import Github
import csv
#创建github对象，需要提供个人访问令牌
g = Github("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")
#获取当前用户
user = g.get_user('LghLcxLjxLxb')
repos=[]
data=[]
for following in user.get_following():
  print(following)
  username=following
#列出当前用户的所有仓库
  for repo in following.get_repos():
    print(repo)
    repos.append(repo)
  data.append([username,repos])
with open('following_repos','w',newline='',encoding='utf-8') as csv_file:
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow(['关注者','仓库'])
  csv_writer.writerows(data)
print('成功')