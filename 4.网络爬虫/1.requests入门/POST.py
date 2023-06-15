import requests
url = 'https://fanyi.baidu.com/sug'

s = input('请输入你要查询的单词:')

data={
    "kw":s
}

#发送post请求
resp =requests.post(url,data=data)
#print(resp.text) #带乱码
print(resp.json())  # 将服务器返回的内容直接处理成json-dict
resp.close()