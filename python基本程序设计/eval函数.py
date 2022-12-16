"""eval函数"""
# 1.eval无参实现字符串转化
s = '1+2+3*5-2'
print(eval(s))  # 16

# 2.字符串中有变量也可以
x = 1
print(eval('x+2'))  # 3

# 3.字符串转字典
print(eval("{'name':'linux','age':18}"))
# 输出结果：{'name':'linux','age':18}

# 4.eval传递全局变量参数,注意字典里的:age中的age没有带引号，说明它是个变量，而不是字符串。
# 这里两个参数都是全局的
print(eval("{'name':'linux','age':age}", {"age": 1822}))
# 输出结果：{'name': 'linux', 'age': 1822}
print(eval("{'name':'linux','age':age}", {"age": 1822}, {"age": 1823}))
# 输出结果：{'name': 'linux', 'age': 1823}

# eval传递本地变量，既有global和local时，变量值先从local中查找。
age = 18
print(eval("{'name':'linux','age':age}", {"age": 1822}, locals()))
# 输出结果：{'name': 'linux', 'age': 18}
print("-----------------")

print(eval("{'name':'linux','age':age}"))