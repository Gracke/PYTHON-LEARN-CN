"""
元字符：
    . -> 匹配到任意字符(除\n) -> pyth\ton >= p,y,t,h,\t,o,n
    \w -> 匹配字母,数字,下划线 -> pyth\ton123 >= p,y,t,h,o,n,1,2,3
    \W -> 匹配非字母,数字下划线 -> pyth\ron >= \r
    \s -> 匹配任意空白字符 -> pyth/ton >= /t
    \S -> 匹配任意非空白字符 -> pyth/ton >= p,y,t,h,o,n
    \b -> 匹配位于开头或者结尾的空字符串 -> python PHP >= 获得PHP中的第一个P
    \d -> 匹配任意十进制数 -> pyth/ton1234 >= 1,2,3,
限定符：
    ? 匹配0次或一次 -> colou?r >= color 或 colour
    + 匹配字符一次或多次 -> colou+r >= colour 或 colouuu····r
    * 匹配前面的字符0次或多次 -> colou*r >= color 或 colouuu···r
    {n} 匹配前面的字符n次 -> colou{2}r >= colouur
    {n,} 匹配前面的字符至少n次 -> colou{2,}r colouur 或 colouu····r
    {n,m} 匹配前面字符最少n次，最多m次 -> colou{2,4}r >= colouur 或colouuur 或 coluuuur
其他字符:
    1.区间字符[]: 匹配[]中所指定的字符 - [0~9] 匹配0到9的数字
    2.排除字符^ : 排除[]中指定的字符 -[^0~9]    排除0到9的数字
    3.选择字符|: 用于匹配|左右的的任意字符 \d{18}|\d{15}   匹配18位数字或者18位数字
    4.转义字符 \. -> \.将作为普通字符
    5.[\u4e00-\u9fa5] 匹配任何一个汉字
    6.分组() 改变限定符的作用  (six|four)th 匹配sixth或fourth
"""

"""
re.match()方法: 用于从字符串的开始位置进行匹配
    re.match(pattern,string,flags=0)
"""
import re
pattern1 = r'\d\.\d{2}'
str1 = 'I study python3.10 ever day'
match1 =re.match(pattern1,str1,re.I)   # re.I不区分大小写
print(match1)

str2 = '3.10python is world'
match2 = re.match(pattern1,str2,re.I)
print(match2)
print('匹配的起始位置:',match2.start())
print('匹配的结束位置:',match2.end())
print('匹配区间的位置元组:',match2.span())
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())

print('-------------------------------------------')

"""
re.search()方法:用于整个字符串搜索第一个匹配的值
        re.search(pattern,string,flags=0)
"""
pattern2 =r'\d\.\d+'
str3 = 'I like python3.10 add python2.10'
str4 = '4.10python I study every day'
str5 = 'I study python every day'
print(re.search(pattern2,str3))
print(re.search(pattern2,str4))
print(re.search(pattern2,str5))

print('-------------------------------------------')

"""
re.findall()方法:用于整个字符串搜索所有符合的正则表达式
        re.findall(pattern,string,flags=0)
"""
pattern3 =r'\d\.\d+'
str6 = 'I like python3.10 add python2.10'
str7 = '4.10python I study every day'
str8 = 'I study python every day'
print(re.findall(pattern3,str6))
print(re.findall(pattern3,str7))
print(re.findall(pattern3,str8))

print('-------------------------------------------')

"""
re.sub()方法:用于实现字符串的替换
        re.sub(pattern,repl.string,count,flag=0)
re.split()方法:与字符串spilt的方法相同
        re.spilt(pattern,repl.string,maxspilt,flag=0)
"""
pattern = '黑客|破解|反爬'
s1 ='学习python的网络爬虫,可以破解和反爬吗'
web = re.sub(pattern,'xxx',s1)
print(web)

s2 ='https://www.baidu.com/&1234&&&rsd?a=????'
pattern_b ='[?|&]'
print(re.split(pattern_b,s2))