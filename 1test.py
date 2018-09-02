import requests

r = requests.get('https://www.baidu.com/')
print(r.status_code)  #看是否可以爬取
print(r.text)
print(r.encoding)#从http header 中猜测的响应内容编码
print(r.apparent_encoding)#从内容中分析出的相应内容编码方式