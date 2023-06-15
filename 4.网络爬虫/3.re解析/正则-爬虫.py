import re
# findall
data1 = re.findall(r"\d+", "我的电话:10086,我的女朋友电话:10010")
# print(data1)

# finditer:匹配字符串中所有内容(返回迭代器）
data2 = re.finditer(r"\d+", "我的电话:10086,我的女朋友电话:10010")
# for i in data2:
#     print(data2)

# search(找到一个结果就返回)返回的是match对象,group()用来拿数据
s = re.search(r"\d+", "我的电话:10086,我的女朋友电话:10010")

# match是从头开始匹配
m = re.match(r"\d+","10086,我的女朋友电话:10010")


# 预加载正则表达式
tar = re.compile(r"\d+")
t = tar.finditer("10086,我的女朋友电话:10010")
for item in t:
    print(item.group())

print('---------------------------------------------------------------------------')

s="""
<div class='jay'><span id ='1'>周杰伦</span></div>
<div class='jj'><span id ='1'>林俊杰</span></div>
<div class='xs'><span id ='1'>许嵩</span></div>"""

obj1 = re.compile(r"<div class='.*?'><span id ='.*?'>.*?</span></div>")
obj2 = re.compile(r"<div class='.*?'><span id ='.*?'>(?P<name>.*?)</span></div>",re.S)
result1 = obj1.finditer(s)
result2 = obj2.finditer(s)
for val in result1:
    print(val.group())
for val in result2:
    print(val.group('name'))