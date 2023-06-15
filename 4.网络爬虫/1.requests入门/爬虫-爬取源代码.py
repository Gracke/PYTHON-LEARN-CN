# 通过编写程序来获取互联网资源
from urllib.request import urlopen

# 打开网址
url = 'http://www.baidu.com/'
resp =urlopen(url)

#读取网址
#print(resp.read().decode('utf-8'))

#另存于html文件中
with open('my_baidu.html','w') as f:
    f.write(resp.read().decode('utf-8'))    #读取页面源代码
