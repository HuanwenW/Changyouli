# 基于bs4库的HTML格式输出

import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
print(demo)

soup = BeautifulSoup(demo, "html.parser")

#prettify()函数能够 结构化 输出标签结构

print(soup.prettify())#输出所有标签结构
