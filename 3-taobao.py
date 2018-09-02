#淘宝商品比价定向爬虫
#淘宝接口&&翻页处理
#静态数据
'''
框架：
1.提交商品收索请求，循环获取页面
2.对每个页面，提取商品名称和价格信息
3.输出数据
'''
import requests
import  re
#获得页面的函数
def getHTMLtext(url):
    try:
        r = requests.get(url ,timeout=30) #控制请求时间timeout为30s
        r.raise_for_status() #确定请求返回状态码正常（200），否则跳出模块
        r.encoding = r.apparent_encoding #转换为python可读取的字符编码
        return r.text #一切都正常的话，返回网页内容
    except:
        return "爬取数据失败！"
#对获得的页面进行解析
def parsePage(ilt,html):
    try:
        plt =re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#价格有小数点由  数字和小数点  构成
        tlt =re.findall(r'\"raw_title\"\:\".*?\"',html) #  *？\" 表示最小匹配,即匹配第一次出现"的位置（系统默认的是最大匹配）
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  #eval函数作用去掉最外层的  引号（双引号或单引号）
            title =eval(tlt[i].split(':')[1])   #用split函数分割获得字符串中 ：后面的部分
            ilt.append([price,title])  #获取信息放到列表中
    except:
        print("解析失败")
#打印爬取内容
def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}" #设置打印模板 长度分别为 4  8  16
    print(tplt.format("序号","价格","商品名称"))  #设置表头
    count =0
    for g in ilt:
        count = count+1
        print(tplt.format(count,g[0],g[1]))
    print("")

def main():
    goods = '书包'
    depth = 3 #爬取页面深度（页数）
    start_url ='https://s.taobao.com/search?q='+ goods
    infoList =[] #输出列表变量
    for i in range(depth):
        try:
#https://s.taobao.com/search?initiative_id=staobaoz_20180808&q=书包
#https://s.taobao.com/search?initiative_id=staobaoz_20180808&q=%E4%B9%A6%E5%8C%85&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
            url = start_url + '&s' + str(44*i)  #相比第一页链接多个&S，每多一页多44
            html = getHTMLtext(url)
            parsePage(infoList,html)
        except:
            continue
        printGoodslist(infoList)
main()