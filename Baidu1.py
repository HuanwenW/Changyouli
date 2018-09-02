#获取  百度/360  搜索关键词提交

import  requests
'''
kv = {'wd':'python'}
r = requests.get("https://www.baidu.com/s", params=kv)#替换关键词参数
print(r.status_code)
print(r.request.url)#  查看替换 关键词为python 后的网址
print(len(r.text))#查看返回信息长度
'''
keyword ="python"
try:
    #kv = {'wd': keyword}
    kv = {'q':keyword}
    #r =requests.get('https://www.baidu.com/s',params=kv)
    r = requests.get('https://www.so.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("loser!")

#相比baidu  ，360只有关键词参数和网址发生变化
