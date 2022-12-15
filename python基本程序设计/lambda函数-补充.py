"""
lambda：匿名函数(省去命名函数的步骤)
    lanmbda 变量 : 实现方法
"""
# def f(str):
#     return len(str.split())

# print(f('hellp python'))
#等价于
# lambda str : len(str.splict())

""" lambda如何调用"""
#1.赋值给变量
# l = lambda str : len(str.split())
# l('hello world')
#2.参数写在后面
# (lambda str : len(str.split()))('hello world')
#3.key=lambda
list = ['python is good','php','go','java']
list.sort(key=lambda str : len(str.split()))
print(list)
#lambda函数作为返回值
# def f(a,b,c):
#     return lambda x : a*x**2 +b*x + c
# g=f(1,2,3)  #分别为a,b,c的值
# print(g(3))



