#获取亚马逊商城商品信息
#与京东不同点：亚马逊对访问网站做了筛查，头部信息为request会被拒绝【20180719测试时，无检查筛选】
import  requests

'''
r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y')
print(r.status_code)
print(r.encoding)
print(r.text)
print(r.request.headers)  #查看我们发给亚马逊网站请求的头部信息，发现我们把告诉亚马逊的服务器我们的访问时由python的requests产生
'''

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    Kv = {'user_agent':'Mozilla/5.0'}#由于亚马逊网站对requests库有判断，所以这里我们需要模拟一个浏览器进行请求，即重新定义了request的头部信息为Mozilla/5.0
    r = requests.get(url, headers=Kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('loser!')
# 20180718  测试是亚马逊网站对头部为request请求的无要判断！原来出错请看第一张第三节ppt课件--亚马逊网站爬取实例


