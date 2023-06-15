import requests
import re
import csv
url = 'http://www.xinfadi.com.cn/getPriceData.html'

# 重新组装参数

headers= {
    "User-Agent":"Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
}
resp = requests.post(url=url, headers=headers)
js_content = resp.json()
obj_content = str(js_content)
# print(obj_content)

tar = re.compile(r".*?'prodName': '(?P<Name>.*?)',.*?'avgPrice': '(?P<avgPrice>.*?)',")

result = tar.finditer(obj_content)
for item in result:
    name = item.group("Name")
    price = item.group("avgPrice")
    with open("菜价.csv",mode='a+') as f:
        writers = csv.writer(f)
        writers.writerow([name,price])

    # print(item.group('Name'))
    # print(item.group('avgPrice'))


