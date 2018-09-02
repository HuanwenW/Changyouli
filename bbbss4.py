#基于bs4库的HTML内容遍历方法

import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
#print(demo)

soup = BeautifulSoup(demo,"html.parser")

#  .contents用于遍历儿子节点，！！返回的是列表类型！！  .children、 .descendants 返回的是迭代类型，只能用于for循环语句中
print(soup.head)  #输出head标签
print(soup.head.contents)#输出head标签的儿子节点

print(soup.body.contents)#输出body标签的儿子节点
print(len(soup.body.contents))#查看body标签儿子节点个数
print(soup.body.contents[1])#查看body标签第2个节点（列表是从0开始计数的）

#  .parent 返回当前节点的父亲标签
#  .parents 返回当前节点的所有先辈节点

#print("title的父标签" + soup.title.parent)#查看title标签的父标签
print(soup.title.parent)#查看title标签的父标签
print(soup.html.parent)#查看html标签的父标签,结果是本身，说明无父标签

#遍历a标签的父标签
for parent in soup.a.parents:
    if parent is None:
        print(parent + "No Parent")
    else:
        print(parent.name)

#对标签树平行遍历(平行遍历仅限于同一个父亲节点)
# .next_sibling、.previous_sibling 平行遍历方法
# .next_siblings、.previous_siblings 是迭代类型，只能用在 for 循环中（eg.  for a  in soup.a.next_siblings）

print(soup.a.next_sibling)#  当前a标签的下一个平行节点
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)#当前a标签的前一个平行节点  ！！返回的是一段文本
print(soup.a.previous_sibling.previous_sibling)  #结果是None，说明再之前无平行节点


