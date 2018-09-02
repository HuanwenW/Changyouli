#国家地理网站篇  网络上好看的图片存储

import requests
import os
'''
path = "E:/PythonData/MOOC/adc.jpg"#给图片找个位置保存
url = 'http://syds.ngchina.cn/resc/picture/banner3.jpg'#图片链接!!切记是右键复制图片链接，而不是粘贴网址
r = requests.get(url)
print(r.status_code)

with open(path, 'wb') as f:
    print(f.write(r.content))
f.close()
'''
url = "http://syds.ngchina.cn/resc/img/difang1.jpg"
root = "E:/PythonData/MOOC/"  #定义根目录
path = root + url.split('/')[-1] #截取图片名字
# 这两步操作是为了保留原图片命名
try:
    if not os.path.exists(root):
        os.mkdir(root)           #判断根目录是否存在，不存在建立
    if not os.path.exists(path):
        r = requests.get(url)     #判断存储地址是否存在，不存在建立
        with open(path ,'wb') as f:
            f.write(r.content)
            f.close()
            print('sccessful')
    else:
        print("已存在")
except:
    print('loser')

