#基于bs4库的HTML内容查找方法

import requests

from  bs4 import BeautifulSoup

import re  #  re库 是正则表达式

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo,'html.parser')

'''
find_all(name,attra,recursive,string,**kwargs)
返回的是一个列表类型，存储查找的结果
name： 对 标签名称   的检索字符串
attrs: 对 标签属性值 的检索字符串，可标注属性检索
recursive: 是否对子孙全部检索，默认True  [是个bool型值]
string: <>....</>中字符串区域的检索字符串
'''
print(soup.find_all('a'))  #检索 a 标签
print(soup.find_all(['a','b'])) #同时检索 a，b标签

#如果给出的是True，将显示soup的所有标签
for tag in soup.find_all(True):
    print(tag.name)
#查找只显示以b开头的标签，   需要要到正则表达式库
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 检索p标签中，包含 course 字符串的信息
print(soup.find_all('p','course'))
# 直接对属性进行约定；以id为link1为例查找
print(soup.find_all(id ='link1'))
#查找id为link的标签  ！！结果为空
print(soup.find_all(id = re.compile('link')))
#属性部分信息匹配， eg.通过link查找包含link1、link2...linkn的信息
print(soup.find_all(id=re.compile('link')))

#第三个参数 requests 验证
print(soup.find_all('a'))
print(soup.find_all('a',requests=False))

#第四个参数 string 验证

print(soup) #查看soup的所有信息
print(soup.find_all(string="Basic python"))#soup中查找一个叫“Basic Python”的字符串

print(soup.find_all(string = re.compile("python")))#部分匹配，查找包含Python的字符串