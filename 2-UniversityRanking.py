#大学排名 本网站是定向爬取， ##中文空格填充居中  ##
'''
程序结构设计
1.从网络上获取大学排名网页内容
2.提取需要的网页内容到合适的数据结构中（核心）
3.利用数据结构展示并输出结果
'''
import requests
from bs4 import BeautifulSoup
import  bs4  #使用标签

def getHTMLtext(url):
    try:
        r = requests.get(url ,timeout=30) #控制请求时间timeout为30s
        r.raise_for_status() #确定请求返回状态码正常（200），否则跳出模块
        r.encoding = r.apparent_encoding #转换为python可读取的字符编码
        return r.text #一切都正常的话，返回网页内容
    except:
        return "爬取数据失败！"
def fillUnivList(ulist,html):
    soup =BeautifulSoup(html,"html.parser")
    #观察网页，发现所有所有内容都在tbody标签中，每所大学信息都在tr标签中
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):   #对便签类型做判断，以防内容中有字符串tr
            tds = tr('td') #要获取的具体内容在td中
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
def printUnivList(ulist,num): #ulist对应主函数中的uinfo
    #print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    #居中对齐！！默认填充是 西文，我们改为中文 chr(12288)
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}" #第二列加{3}，是表明填充空格形式不是默认，而是自定义的第三个参数
    print(tplt.format("排名", "学校名称", "总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        #print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
        print(tplt.format(u[0], u[1], u[2],chr(12288)))
    print("Suc"+ str(num))

def main():
    uinfo =[]#网页信息存在列表中
    url ="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html =getHTMLtext(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,31)#爬前31所大学
print(main())