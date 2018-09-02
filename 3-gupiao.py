#股票数据定向爬虫
#动态数据

#出
'''
框架：
1.提交商品收索请求，循环获取页面
2.对每个页面，提取商品名称和价格信息
3.输出数据
'''
import requests
from bs4 import BeautifulSoup
import traceback
import  re

#获得页面的函数
def getHTMLtext(url):
    try:
        r = requests.get(url)
        r.raise_for_status() #确定请求返回状态码正常（200），否则跳出模块
        r.encoding = r.apparent_encoding #转换为python可读取的字符编码
        return r.text #一切都正常的话，返回网页内容
    except:
        return "爬取数据失败！"
#获得股票的信息列表
def getStockList(lst,stockURL):
    html = getHTMLtext(stockURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all('a')#内容链接在a 标签中
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])#正则匹配 6位数股票代码
        except:
            continue

    return "获取股票信息失败"

#获得单个股票的信息，并保存在文件中
def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL +stock + ".html"
        html = getHTMLtext(url)
        try:
            if html =="": #判断是否为空页面
                continue
            infoDict = {}  #字典
            soup =BeautifulSoup(html,"html.parser")
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            #print("stockInfo:", stockInfo)
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]

            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt') #dt键域
            valueList = stockInfo.find_all('dd')#dd值域
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            #print("error")
            traceback.print_exc()  #获取错误信息，当stockInfo没获取到div标签中的内容事，报'NoneType' object has no attribute 'find_all'错
            continue
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file ='E://BaiduStockInfo1.txt'
    slist =[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
main()