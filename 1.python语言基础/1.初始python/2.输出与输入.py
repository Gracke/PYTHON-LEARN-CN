"""
print() 方法用于打印输出，最常见的一个函数。
"""
print("hello,world")

a = 1
b = 'runoob'
print(a,b)

print("aaa""bbb")
print("aaa","bbb")

print("www","runoob","com",sep=".")  # 设置间隔符


"""
input() 函数接受一个标准输入数据，返回为 string 类型。
"""
a = input("请输入任意字符:")
# 检测输入类型
print(type(a))