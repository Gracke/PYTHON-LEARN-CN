from lxml import etree
import requests
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse("test.html",parser=parser)

# /h3[1] xpath支持索引
result1 = tree.xpath('/html/body/div/div/h3[1]/text()')
# h3[@class="titles"] 找出h3的属性是titles的标签
# /@class
result2 = tree.xpath('/html/body/div/div/h3[@class="titles"]/text()')
print(result1)
print(result2)
print("--------------------------------------------------------------")
result3 = tree.xpath('/html/body/div/div//div/a')
for tree1 in result3:
    res = tree1.xpath('./span/text()')
    # /@href 取href的值
    res2 = tree1.xpath('./@href')
    print(res)
    print(res2)