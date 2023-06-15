"""
html是xml的一个子集
<book>
    <id>1</id>
    <name>1.23</name>
    <price>1.23</price>
    <author> // 副节点
        <nick>周杰伦</nick>
        <nick>林俊杰</nick>
    </author>
</book>
每一个标签都是节点
"""
from lxml import etree
text = '''
<root>
    <resultcode>200</resultcode>
    <reason>Return Successd!</reason>
    <result>
        <province>湖南</province>
        <city>张家界</city>
        <areacode>0744</areacode>
        <zip/>
        <company>联通</company>
        <card/>
    </result>
    <error_code>0</error_code>
</root>
'''

tree = etree.XML(text)
# * 当前节点的任意节点
result1 = tree.xpath("/root/result/*/text()")
# // 找出所有节点(包括后代节点）
result2 = tree.xpath("/root/result//text()")
print(result1)
print(result2)