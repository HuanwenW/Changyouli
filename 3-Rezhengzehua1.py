import  re

### match对象 是一次匹配的结果，包含匹配的很多信息
'''
re.search(pattern,string,flags = 0)
意义：在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
第一个参数pattern：正则表达式的字符串或原生字符串表示
第二个参数string：待匹配字符串
第三个参数flage:正则表达式使用时的控制标记
'''
# 匹配邮政编码
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

'''
re.match(pattern,string,flags = 0)
意义：从一个字符串的开始位置起匹配正则表达式，返回match对象
参数意义同上
'''
match1 = re.match(r'[1-9]\d{5}','100081 BIT')
#此处邮政编码位置换前面了，因为match是从第一个位置匹配，第一个位置不匹配将直接返回空
if match:
    print(match.group(0))

'''
re.findall(pattern,string,flags = 0)
意义：搜索字符串，以列表类型返回全部能匹配的子串
参数意义同上
'''
ls  = re.findall(r'[1-9]\d{5}','100081BIT USB100083')
print('匹配的字符串有',ls)

'''
re.split(pattern,string,maxsplit = 0，flags = 0)
意义：将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
maxsplit：最大分割数，剩余部分作为最后一个元素输出
其它参数意义同上
'''
ls1 = re.split(r'[1-9]\d{5}','100081BIT USB100083')
print('不加maxsplit参数，默认全部分割，结果为：',ls1) #输出结果是除了匹配的  邮政编码剩余部分

ls2 = re.split(r'[1-9]\d{5}','100081BIT USB100083',maxsplit=1)
print('只匹配第一个字符串的结果为：',ls2) #第二个不再匹配分割

'''
re.finditer(pattern,string,maxsplit = 0，flags = 0)
意义：搜索字符串，返回一个匹配结果的 迭代类型，每个迭代元素是match对象
参数意义同上
'''
print('迭代输出形式:')
for m in re.finditer(r'[1-9]\d{5}','100081BIT USB100083'):
    if m:
        print(m.group(0))
'''
re.sub(pattern,repel,string,count = 0，flags = 0)
意义：在字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
repel:要替换的字符串--新的字符串
count：匹配的最大替换次数
其他参数意义同上
'''
str = re.sub(r'[1-9]\d{5}','zipcode','100081BIT USB100083')
print('替换后的字符串为：',str)