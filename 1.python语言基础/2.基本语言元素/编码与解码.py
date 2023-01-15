"""
字符串的编码与解码：
    首先要搞清楚，字符串在Python内部的表示是unicode编码，
    因此，在做编码转换时，通常需要以unicode作为中间编码，
    即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
"""
# 编码
g = '数字是什么'
code_GBK = g.encode('GBK')
print(code_GBK)
code_UTF8 = g.encode('utf-8')
print(code_UTF8)
# 解码
print(bytes.decode(code_UTF8,'utf-8'))
print(bytes.decode(code_GBK,'gbk'))