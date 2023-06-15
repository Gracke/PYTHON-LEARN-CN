"""
1.定位到2023必看热片
2.从2023必看热片提取子页面的链接地址
3.请求子页面的链接地址，拿到我们想要的下载地址
"""
import re
import requests
url="https://www.dy2018.com/"

resp = requests.get(url,verify=False) # verify:在请求的时候不验证网站的ca证书
resp.encoding='gb2312'

obj1 = re.compile(r"2023必看热片.*?<ul>.*?(?P<URL>.*?)</ul>",re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1></div>'
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<magnet>.*?)">magnet',re.S)
re1 = obj1.finditer(resp.text)
re2 = obj2.finditer(resp.text)

data_web = []
for item in re1:
    i = item.group('URL')
    for tar in re2:
        # 获取子页面的html
        t1 = tar.group('href')
        # 将主页面的url与子页面的html衔接，实现子页面的url
        son = url + t1.strip('/')
        # 建一个空列表，把加进去
        data_web.append(son)

for son_url in data_web:
    resp1 = requests.get(son_url)
    resp1.encoding = 'gb2312'
    re3 = obj3.search(resp1.text)
    print(re3.group('name'))
    print(re3.group('magnet'))

