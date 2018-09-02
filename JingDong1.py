#获取京东商品信息
import  requests
'''
#  最初测试是否可爬取信息
r = requests.get("https://item.jd.com/2967929.html")#荣耀8
r = requests.get("https://item.jd.com/7694047.html")#荣耀9i
print(r.status_code)  #查看返回状态码
print(r.encoding)    #查看网站编码
print(r.text[:1000])  #拉去网站内容
'''
url = "https://item.jd.com/7694047.html"
try:
    r = requests.get(url)
    r.raise_for_status()  #返回状态是200不产生异常，否则从跳出try模块
    r.encoding = r.apparent_encoding  #不管原网站编码是啥，我们都改为python可读取的编码形式
    print(r.text[:1000])
except:
    print("loser")
