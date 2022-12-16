"""字符串的编码与解码"""
# 编码
g = '数字是什么'
code_GBK = g.encode('GBK编译规则')
print(code_GBK)
code_UTF8 = g.encode('utf-8')
print(code_UTF8)
# 解码
print(bytes.decode(code_UTF8,'utf-8'))
print(bytes.decode(code_GBK,'gbk'))