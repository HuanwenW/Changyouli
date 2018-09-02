# 提取HTML中所有URL链接

#思路：1) 搜索所有<a>标签
#     2) 解析<a>标签格式，提取href后的链接内容

from bs4 import BeautifulSoup

import requests

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):  ##find_all  查找所有 a 标签
    print(link.get('href'))

