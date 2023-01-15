"""
变量的作用域
"""
# 例如: a为全局变量,b为局部变量
a =100

def func1():
    print(a)

def func2(b):
    global a
    return a + b



print(func2(10))
# func1()  NameError: name 'func' is not defined
"""
func2() 会报错,因为函数func2是封装的,函数体内执行的函数是一个新的作用域,
函数体内的一切操作只作用于自己体内
但可以使用global关键字,可以在函数体内使用全局变量,因为变量被声明了
"""

print('------------------------------------')

# 嵌套函数的作用域
def foo():
    b = 'hello'
    # Python中可以在函数内部再定义函数
    def bar():  # 对于bar()来说,变量b属于嵌套作用域,在bar()体内是可以访问变量b,不需要额外声明
        c = True    # 变量c在bar()中属于局部作用域
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined -> 变量c是foo()体内,bar()体外.
    # 因此,c是作为bar()局部变量，局部变量无法在函数体外被访问

if __name__ == '__main__': # 在if __name__ == '__main__'内定义的变量为全局变量
    a = 100     # a 为全局变量,属于全局作用域
    # print(b)  # NameError: name 'b' is not defined
    foo()
"""
事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，
前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些标识符，
我们之前用过的input、print、int等都属于内置作用域。
"""

print('------------------------------------')

def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()       # foo()执行的是foo()函数体内的操作,局部变量a=200
    print(a)  # 100  # 这个a是全局变量,a=100