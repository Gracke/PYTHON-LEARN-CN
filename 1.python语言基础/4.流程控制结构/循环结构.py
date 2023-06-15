"""
for循环语句:用来遍历(迭代)序列(tuple/str/list/dict/set)
    1.for语句可以不通过下标的方式来依次访问序列的每一个元素
    2.用for语句来迭代dict时，只访问键，其他序列访问结果相同
    3.range()-依次遍历所有数值
"""
for i in (11, 21, 31, 41):
    print(i)
for z in [1, 2, 3, 4]:
    print(z)
for x in {'name': 'qaq', 'username': 'Gracke'}:
    print(x)
for p in range(1, 10):
    print(p)
example = 'abcd'
for i, j in enumerate(example):
    print(i, j)

print('----------------for循环的嵌套------------------------')

"""
for循环结构的嵌套
"""
a = ['a', 'b', 'c', [1, 2, 3], (11, 22, 33)]
for i in a:
    if isinstance(i, float):
        for x in i:
            print(x)  # 迭代变量a的序列是否具有float类型，若存在，则返回，反之，则跳过往下执行
    elif isinstance(i, tuple):
        for y in i:
            print(y)  # 迭代变量a的序列是否具有bool类型，若存在，则返回，反之，则跳过往下执行
    elif isinstance(i, str):
        for z in i:
            print(z)

print('----------------while循环结构-------------------------')

"""
while循环结构(会根据条件进行循环)， 可以配合else运用
"""
a = 0  # 变量 a = 0
while a < 6:  # while的前置条件需满足 a < 6,才可以往下运行
    print(a)  # 满足while的条件，才能输出a变量，再往下运行
    a += 1  # a = a + 1  在变量a经过打印之后，进行+1，再回到while的条件进行循环
else:  # 若没有变量增加值,则数值一直会保持原始变量值不断的运行下去
    print('运行完毕')  # 当while的循环结束，等同于a的变量的增加已无法再执行while，使循环停止,运行else

"""
break，跳出while和for的循环体,终止循环。
continue，跳过当前循环块的剩余语句，再进行下一次循环。
"""
# for循环
for i in ('python'):
    if i == ('o'):
        print(i)
    elif i == ('n'):
        break  # 当循环到break，终止循环
        print(i)  # 在elif的条件下，print()若在elif的缩进里面，则为elif的条件，若不在，则单独执行。
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in '12345':
    if x == '3':
        continue  # continue在满足if的条件下，会终止此次循环，则返回值会不会打印字符'3'
    print(x)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for y in ['厄瓜多尔', '卡塔尔', '英格兰', '伊朗']:
    if y == '卡塔尔':
        continue
    print(y)  # 先遍历序列的元素，当遍历到if的条件语句后，此次循环跳过返回值(不打印),进行下一次循环
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# while循环语句
p = 0
while p < 6:
    p += 1
    print(p)
    if p == 5:
        break  # 终止循环
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
j = 0
while j < 8:
    j += 1  # 若没有此条件，while语句会不断进行int:0的循环
    if j == 5:
        continue  # 当 j的变量不断增加时，当循环到j=5时，跳过print，进行下一次循环
    print(j)

print('----------------pass 空语句---------------------------')

"""
pass 空语句，保持程序结构的完整性
"""
for i in range(0, 10):
    pass

for v in range(0, 10):
    pass
