"""
递归；
    特点；1.调用自身
        2.结束条件
"""
def func1(x):
    if x > 0:
        func1(x-1)    #当函数运行此行的func1，函数重新开始循环,调用函数func1
        print(x)

func1(3)

def func2(x):
    if x > 0:
        print(x)
        func2(x-1)    # #当函数运行此行的func2，函数会返回重来，调用函数func2

func2(3)

def list(list_a):
    if len(list_a) == 1:
        return list_a[0]
    else:
        return list_a[0] + list(list_a[1:])

print(list([1, 3, 5, 7, 9]))

"""汉诺塔问题"""
# def hanoi(n, a, b, c):   #参数的意义；将n个盘子从a经过b运到c
#     if n > 0:
#         hanoi(n-1, a, c, b)
#         print('moving from %s to %s' %(a,c))  #这是第n个盘从子a直接运到c，可以直接输出
#         hanoi(n-1,b, a, c)
#
# hanoi(3, 'A', 'B', 'C')

# def int(a,b):
#     print(a+b)
# int(a,b)

