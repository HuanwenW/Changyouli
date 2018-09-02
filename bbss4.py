#BeautifulSoup使用原理：把所你给的文档当做一锅汤，并进行煲制
#也可以理解为：Beautiful Soup库是解析、遍历、维护网页“标签树”的功能库
#例子：获取http://python123.io/ws/demo.html 源代码

import requests
# from bs4 import beautifulSoups4！！此种写法错误  表示的是一个包！！

from bs4 import BeautifulSoup #导入bs4【是beautifulSoups4的简写】库中的一个BeautifulSoup类

#方法一：用之前学的request库获取内容
r = requests.get("https://python123.io/ws/demo.html")
print(r.text)

demo = r.text
soup =BeautifulSoup(demo,"html.parser") #参数 前者是需要BeautifulSoup解析的html格式的信息 后者是前者的解析器
print(soup.prettify()) #输出所有标签结构？

print(soup.title)#获取页面titlle

#获取a标签（内容）
tag =soup.a
print(tag)

#获取a标签name
a_name = soup.a.name
print("a标签名字：" + a_name)

ap_name =soup.a.parent.name
print(ap_name)#获取a的父亲标签name

app_name = soup.a.parent.parent.name
print("a父亲的父亲的标签名字：" + app_name)#获取a父亲的父亲的标签name

#查看a标签属性
a_attributes =tag.attrs
print(a_attributes)

print(tag.attrs['class'])#查看a标签中 class 属性的值 ##输出结果可以看出，class属性是个列表，列表的第一个元素是py1
print(tag.attrs['href'])#查看a标签中 href 属性的值
print(type(tag.attrs))#查看  标签属性  的类型  ##结果看出  是个字典类型

#查看 a 标签的  信息
print(soup.a.string)
print(soup.p.string)#查看 p 标签的  信息
print(soup.body.string)#查看 body 标签的  信息

#标签内  注释  内容
newsoup = BeautifulSoup("<b><!--The demo python mmm--></b><p>abc Ha Ha</p>","html.parser")
print(newsoup.b.string)  #输出发现   并没有对 有注释标记的  ！--  进行标记  ，若需要显示，需要做特殊处理（但很少用）
print(newsoup.p.string)
