import requests
from lxml import etree
import csv
url = 'https://www.zbj.com/search/service/?l=0&kw=python&r=2'

headers ={
    "User-Agent":"Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
}

resp = requests.get(url,headers=headers)


html = etree.HTML(resp.text)
count = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div')
for item in count:
    price = item.xpath('./div/div[2]/div[1]/span/text()')
    name = item.xpath('./div/div[2]/div[2]/a/text()[1]')
    company = item.xpath('./div/a/div[2]/div[1]/div/text()')
    with open('python_company.csv','a+') as f:
        writers = csv.writer(f)
        writers.writerow([company,name, price])


