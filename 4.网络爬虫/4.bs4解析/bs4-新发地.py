"""
1.拿到页面源代码
2.使用bs4进行解析
"""
import requests
from bs4 import BeautifulSoup
import csv
url = "http://www.xinfadi.com.cn/priceDetail.html"
headers= {
        "User-Agent":"Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"

}
resp = requests.get(url,headers=headers)

# 解析数据
# 1.将数据交给美味汤处理，生产bs对象
page = BeautifulSoup(resp.text, "html.parser")
# 2. 从bs4对象中查找数据

# find(标签,属性=值) 找一个对象
# find_all(标签,属性=值) 找所有对象
table = page.find("table", border="0", cellspacing="0", cellpadding="0")
table1 = page.find("table", attrs={"broder":"0","cellspacing":"0","cellpadding":"0"})



#拿到所有数据
trs = table.find_all("tr")
for item in trs:
        ths = item.find_all("th") # 拿到每行中的所有td
        name =ths[2].text #.text 表示所有拿到被标签标记的内容
        min_price = ths[3].text
        average_price = ths[4].text
        max_price = ths[5].text
        size = ths[6].text
        origin = ths[7].text
        data = ths[9].text
        #print(name,min_price,average_price,max_price,size,origin,data)
        with open('test.csv', mode='w') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow([name,min_price,average_price,max_price,size,origin,data])

