import requests

url = 'https://cn.bing.com/search?q=周杰伦'

"""
伪装客户端发送请求:
User-Agent 首部包含了一个特征字符串，
用来让网络协议的对端来识别发起请求的用户代理软件的应用类型、操作系统、软件开发商以及版本号。
"""
headers ={
    "User-Agent":"Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
}

resp = requests.get(url,headers=headers)

print(resp)
print(resp.text)    #读取页面源代码
resp.close() # 关闭访问