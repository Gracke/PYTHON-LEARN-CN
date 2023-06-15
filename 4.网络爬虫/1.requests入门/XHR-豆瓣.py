import requests

url = 'https://movie.douban.com/j/chart/top_list'

list = [_ for _ in range(0,100,20)]
for i in list:
        pass

#重新组装参数
params ={
'type': '24',
'interval_id': '100:90',
'action':'',
'start':i,
'limit': 20,
}
headers= {
        "User-Agent":"Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"

}
resp = requests.get(url=url,params=params,headers=headers)
print(resp.json())
resp.json()