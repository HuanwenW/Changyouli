#IP地址归属地的自动查询

import requests

#url = 'http://m.ip138.com/ip.asp?ip=ipaddress'
url = 'http://m.ip138.com/ip.asp?ip='
####两个url都不出错，还不知道原因
try:
    r = requests.get(url+'192.168.1.127')#此处是自己的ip
    r.raise_for_status()
    r.encoding =r.apparent_encoding
    print(r.text[-500:])
except:
    print("loser")
