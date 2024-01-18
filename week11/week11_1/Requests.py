import requests
from bs4 import BeautifulSoup
#发送get请求
response = requests.get("https://baidu.com")
#获取网页内容
html_content = response.text
#打印网页内容
#print(html_content)
#使用Beautiful Soup解析网页内容HTML
soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
#查找特定标签
title = soup.title 
print('标题',title.text)
#查找所有链接
links = soup.find_all('a')
for link in links:
  print(link.get('href'))