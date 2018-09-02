import requests

def getHTML(url):
    try:
        r = requests.get(url, timeout=30) #请求链接
        r.raise_for_status()#如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding #确保解码正确
        return r.text
    except:
        return "异常"
if __name__=="__main__":
    url = 'http://www.baidu.com'
    print(getHTML(url))

