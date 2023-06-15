"""
1.定义列表
2.列表的下标
3.列表的取值
"""
list_1 = 10, 20, 30, [66, 99], '芥兰'
print(list_1[4])
# print(list_1[1][2])

print('----------------------------------------------------')

"""
列表的长度-len()-当只有一个整体的时，一个整体的存在count
更新的列表的值
列表的加法与乘法
字符串的拼接
"""
list_2 = [10, 20, 30, 40, 50]
list_3 = [10, 20, 30], 60, 'fish'
list_4 = [1, 2, 3, 4]

# print(len(list_2))
# print(len(list_3))

# list_2[2] = 66
# list_2[3] = '排球'
# print(list_2)

# print(list_2 + list_4)
# print(list_4*3)
# print('芥兰'*2)

# 列表的切片取值
list_5 = [10, 20, 30, 40, 60, 70, 80, 90]
# print(list_5[0:3])
# print(list_5[0:])
# print(list_5[:])
# print(list_5[-3:-1])
# print(list_5[-6:-1:2])
# print(list_5[-3:-6:-1])

print('----------------------------------------------------')

"""
列表的关键字
1.del 关键字 --删除计算机(内存)当中 a 变量,也可以删掉指定值 
2.append--用于向‘列表’末尾添加元素,无返回值
"""
P = ['s', 'f', 'd', 3]
# del P
# del P[1]
# print(P)

# P.append(4)
print(P)        #append没有返回值

print('----------------------------------------------------')

"""
1.列表的操作方法
  insert函数是用于向列表插入元素,无返回值
  第一个参数是插入的位置，第二个是插入的元素
2.clear 函数用于将列表清空
"""
list_6 = [1, 2, 3, 4, 5]
list_6.insert(0, 99)
print(list_6)


# list_6.clear()
# print(list_6)C
# print(len(list_6))

print('----------------------------------------------------')

"""
1.remove函数-从列表移除'定位元素'，无返回值
(若列表有重复元素，则以第一个处理)
2.pop函数-用于移除相对'位置'(索引)的元素，默认为列表最后一个位置  #pop可以直接输出,若增加一个变量，则返回被移除的值
"""
list_a = [11, 22, 11, 44, 55, 22]
# list_a.remove(22)
# print(list_a)

# list_a.pop(2)
# print(list_a)

print(list_a.pop(2))
print(list_a)

print('----------------------------------------------------')

"""
index函数--返回所匹配的元素索引，第一个函数待查找，第二个查找起始范围，第三个查找结束范围
reverse函数-将列表反向排列,无返回值
"""
K = ['hello', 'world', 'hello', 'python']
R = K.index('hello')
print(R)

#  print(K.index('hello', 1, 3))
# K.reverse()
# print(K[::-1])

print('----------------------------------------------------')

"""
extend用于在列表的末尾添加另一个列表
与append的区别:
append的括号内是'整体'运输,且只能运输一个整体。extend是单纯的元素输出(且括号内必须用[ ]),无返回值。
"""
f = [1, 2, 3, 4]
b = [11, 22, 33]

# f.append([11])  # append的函数是的列表的'数值'，只能是添加一个数值，无返回值
# print(f)

f1 = f.extend([11, 22, 33])
print(f1)


print('----------------------------------------------------')

"""
copy函数用于创造列表的副本
"""
c = ['芥兰', 'tomato', '芥兰', 'tomato']
v = c.copy()
del c
print(v)  # 删掉c[1]后，输出c

print('----------------------------------------------------')

"""
sort函数
用于将列表进行排序
常见ASCII码大小规则0~9<A~Z<a~z
sorted函数:在sort上创建了一个新列表
"""
m = ['Hello', 'Hello', '我', 'world', '1']
n = [6, 5, 4, 3, 2, 1]
# m.sort()
print(m)    #sort函数无返回值

# 先排序， 后reverse将列表反向排列
# n.sort(reverse=True)
# print(n)

# 忽略大小写进行比较
# m.sort(key=str.lower)
# print(n)

#sorted函数-建立一个新列表进行排序
m1 = sorted(m,reverse=True)
print(m1)
print('----------------------------------------------------')

"""
count函数
统计某个元素在列表出现的次数
"""
j = ['hello', 'hello', '我', 'world', '1']
r = j.count('hello')
print(j.count('hello'))

print('----------------------------------------------------')
"""列表的遍历"""
lst = ['python','java','golang','php']
#for循环遍历
for item in lst:
    print(item)
#遍历列表的索引
for i in range(len(lst)):
    print(i)
#运用for与enumerate遍历 元素与索引
for index,value in enumerate(lst):
    print(index,value)
print('----------------------------------------------------')

"""列表生成式"""
# list1 = [item for item in range(1,11)]  #前面的item是表达式,后面的item是循环变量
# print(list1)
# list2 = [item*item for item in range(1,11)]
# print(list2)
import random
list3 = [random.randint(1,50) for _ in range(10)]   # _为变量
print(list3)
# #增加筛选条件
# list4 = [i for i in range(1,30) if i%2==0] 后面可用if语句筛选条件
# print(list4)

