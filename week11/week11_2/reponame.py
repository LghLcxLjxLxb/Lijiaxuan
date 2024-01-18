import requests
# 个人访问令牌
token = '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'
# API请求的URL
url='https://api.github.com/LghLcxLjxLxb/Lijiaxuan'
# 添加个人令牌到访问头部
headers={
  'Authorization':f'token {token}'
}
# 发送访问请求
response=requests.get(url,headers=headers)
# 检查是否访问成功
if response.status_code == 200:
  # 解析响应的json数据
  repos = response.json()
  # 打印仓库名
  for repo in repos:
    print(repo['name'])
else:
  print(f'API请求失败，状态码：{response.status_code}')