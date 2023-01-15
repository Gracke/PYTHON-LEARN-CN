"""
1.元组是一种数据容器，使用小括号 () 表示，
其使用场景与列表相似.
唯一区别是元组不可变----t[1] = 'xx' 不能返回(报错)
2.元组的元素类型不统一
"""
t = ("不吃鱼", 2, 3.14, [11, 22, 33])
# print(t)
print(t[3][1])
print(t[1:3])

"""

元组的拼接
"""
t1 = ('芥兰', 11, 3)
t2 = ('不吃鱼', [22, 33, 44])
# t3 = t1 + t2
# t3[4][0] = 'cs'

# print(t3)

print('-----------------------------------')
"""
元组，列表，字符串的共同操作
len()
max()
min()
"""
a = '1, 2, 3, 4'
b = (11, 22, 33, 44)
c = ['a', 'b', 'c']
print(len(a))
print(max(b))
print(min(c))

print('-----------------------------------')

"""
元组的注意事项以及乘号的运用
"""
# 元组可以不带括号
r1 = 1, 2, 3, 4
r2 = (11, 22, 33, 44)
print(r1)
print(r2)
# 元组必须有逗号
r3 = (10)
r4 = (10,)
print(r3)
print(r4)

print('-----------------------------------')

"""元组的遍历"""
t3 = ('Python','Java','PHP','Golang','C++',)
#range
for i in range(len(t3)):
    print(i,t3[i])
print('-----------------------------------')
#enumerate
for i,j in enumerate(t3):
    print(i,j)

print('-----------------------------------')

"""元组生成式"""
t4 = (i for i in range(1,5))
print(t4)   #   <generator object <genexpr> at 0x000001DAC4372260> 生成器对象

# 生成器对象转换
# print(tuple(t4))    #-> (1, 2, 3, 4, 5, 6, 7, 8, 9)

#for 循环遍历
# for i in t4:
#     print(i)

# __next__()方法,遍历出一个，元组内少一个元素
print(t4.__next__())
print(t4.__next__())
print(t4.__next__())
print(t4.__next__())
print('···········')
for i in t4:
    print(i)



