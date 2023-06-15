import re
import requests
import csv
url = "https://movie.douban.com/top250"

headers ={
 "User-Agent":"Mozilla/5.0 (X10; Mac x86_64) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/538.36 Edg/108.0.1462.46"
}

tar = requests.get(url=url,headers=headers)

page_content = tar.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
               r'</span>.*?<p class="">.*?<br>.*?(?P<year>.*?)&nbsp.*?'
                 r'<div class="star">.*?"v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<number>.*?)人评价</span>',re.S)
result = obj.finditer(page_content)
with open("web_data.csv",mode='w',encoding="utf-8") as f:
    csv_write =csv.writer(f)
    for item in result:
    # print(item.group('name'))
    # print(item.group('year').strip())
    # print(item.group('score'))
    # print(item.group('number'))
        dic =item.groupdict()
        dic['year'] = dic['year'].strip()
        print(dic)
        csv_write.writerow(dic.values())
    


