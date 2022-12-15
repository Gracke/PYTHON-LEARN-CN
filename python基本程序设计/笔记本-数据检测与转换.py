"""
数据类型的检测-type()
"""
a1 = '我'    #-str
a2 = 123    #-int
a3 = [1,2,3,4]  #-list
a4 = {1,2,3,4}  #-set
a5 = {'姓名' : '张增捷'} #-dict
a6 = 3.14   #-float
a7 = (1,2,3,4)  #tuple
a8 = True   #-bool
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))
print(type(a6))
print(type(a7))
print(type(a8))

print('----------------------------------------------------')

"""
数据的强制转换:
    str()-将'任何'的数据类型转化成字符串类型  
"""
b1 = '我'    #-str
b2 = 123    #-int
b3 = [1,2,3,4]  #-list

b11 = str(b3)
print(b11,type(b11))
b33 = str(b3)
print(str(b3), type(b33))

print('----------------------------------------------------')

"""
数据的强制转换:
    int()----可以把其他数据类型转化成整型
    float()--可以把其他数据类型转化成浮点型
notice:
1.数字类型可以相互转化
2.字符串必须为纯数字(负号可以，小数点不行)才能转换成数字类型
3.只有字符串可以转化成数字类型
"""
c1 = '1234'
c2 = 1234
c3 = 3.14159621
c4 = True
c1_int = int(c1)
c1_flo = float(c1)
c2_flo = float(c2)
c3_int = int(c3)
c4_int = int(c4)
print(c1_int, type(c1_int))     #将字符转化成整型
print(c1_flo, type(c1_flo))     #字符转化成浮点型
print(c2_flo, type(c2_flo))     #整型转化成浮点型
print(c3_int, type(c3_int))     #浮点型转整型
print(c4_int, type(c4_int))     #布尔值转整型

print('----------------------------------------------------')

"""
数据的强制转换:
        1.bool()-将其他类型转化成布尔值，返回True&False
        2.数据容器若为空，则返回false
        3.int=0时，返回false，其他条件为True
        4.floa=0.0时，返回false，其他条件为True
"""
d1 = ()
d2 = []
d3 = {}
d4 = set()
d5 = ''
print(bool(d1))
print((bool(d2)))
print(bool(d3))
print(bool(d4))
print(bool(d5))
print('----------------------------------------------------')
print(bool(0))
print(bool(0.0))

print('----------------------------------------------------')

"""
数据的强制转换:list()
    1.数字类型不能转化成list
    2.字符串转list，将str容器内的每一个元素转化成列表内的元素
    3.元组转列表，将tuple容器内器内的每一个元素转化成list的元素
    4.集合转list，将set容器内的每个元素转化成无序（随机排列）的list元素  
    5.字典转list，只返回键 
"""
r1 = '1234'
print(list(r1))
r2 = (1,2,3,4,'love')
print(list(r2))
r3 = {'姓名' : '不吃鱼'}
print(list(r3))
r4 = {1,2,3,4,'a','b'}
print(list(r4))

print('----------------------------------------------------')

"""
数据的强制转换:tuple()
        1.只有数据容器才能转化成元组，(int,float,bool不是数据容器)
        2.字符串转元组时，将str的元素转化成元组内的元素，且每个元素都会添加''
        3.list转元组时，将list元素转化成元组内的元素
        4.set转元组时，将set元素转化成乱序的元组内元素
        5.dict转化元组时，只返回键
"""
t1 = '1234'
print(tuple(t1))
t2 = [1,2,3,4,'qaq']
print(tuple(t2))
t3 = {11,'噢',33}
print(tuple(t3))
t4 = {'姓名':'qaq','年龄':'20'}
print(tuple(t4))

print('----------------------------------------------------')

"""
数据的强制转换:set()
        1.set()只转换数据容器类型
        2.list转化时会乱序
        3.str转换时会乱序
        4.tuple转化时会乱序
        5.dict转化时，只返回键，但键也会乱序        
"""
q1 = '1234'
print(set(q1))
q2 = [1,2,3,4]
print(set(q2))
q3 = (1,2,3,4)
print(set(q3))
q4 = {'qq':'weixi',
      'time':'13:30',
      'date':'2021/11/17'}
print(set(q4))

print('----------------------------------------------------')

"""
数据的强制转换:dict()
            1.dict只能转化数据容器
            2.str无法转化dict
            3.set无法转化dict
            4.list转化dict，list必须为等长的二级容器，且子容器内必须为两个元素，才能转化dict
            5.tuple转化成dict，tuple必须为等长的二级容器，且子容器必须为两个元素，才能转化成dict
"""
l1 = [[1,2],['爱好','排球']]
print(dict(l1))
l2 = (('qaq','user'),('dddd',1111))
print(dict(l2))

print('----------------------------------------------------')

"""
判断数据的已知类型:isinstance
            1.isinstance()用来判断一个对象是否为已知类型
            它的返回值是bool值
            2.isinstance(对象，对象类型)
"""
h1 = '我'    #-str
h2 = 123    #-int
h3 = [1,2,3,4]  #-list
h4 = {1,2,3,4}  #-set
h5 = {'姓名' : '张增捷'} #-dict
h6 = 3.14   #-float
h7 = (1,2,3,4)  #tuple
h8 = True   #-bool
print(isinstance(h1,str))
print(isinstance(h3,(str,dict,list,bool)))