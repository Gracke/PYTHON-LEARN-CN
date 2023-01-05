"""
特殊方法：
        1.__add__() 执行加法运算
        2.__sub__() 执行减法运算
        3.__lt__(),__le__()  分别执行 <,<=
        4.__gt__(),__ge__()  分别执行 >,>=
        5.___eq__() 执行==, __ne__()  执行!=
        7.__truediv__() 进行/运算(非整除运算), __floordiv__() 进行//运算(整除运算)
        8.__mul__() 执行乘法运算，__mod__() 执行%(取余)运算. __pow__()执行**运算
"""
#eg-1
a=10
b=20
print(a+b)
print(a.__add__(b))
#eg-2
class number:
    def __init__(self,int,float):
        self.int =int
        self.flo =float
    def __lt__(self,other):
        return self.int < other.int
if __name__ == '__main__':
    num1 =number(11,1.1)
    num2 =number(22,2.2)
    print(num1<num2)

print('--------------------------------------------')

"""
特殊属性：
        1.obj.__dict__ 对象的属性字典
        2.obj.__class__ 对象的所属类
        3.calss.__bases__ 类的父类元组
        4.calss.__base__ 类的父类
        5.calss.__mro__ 类的层次结构
        6.class.__subclasses__() 类的子类列表
"""
#eg
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age =age

if __name__ == '__main__':
    a = A()
    b = B()
    c = C('GARKCE',18)
    print(c.__dict__)
    print(c.__class__)
    print(A.__base__)  # 是的父类是该类本身
    print(C.__bases__)
    print(C.__base__)   #如果是多继承，则结果是第一个父类
    print(C.__mro__)
    print(A.__subclasses__())       #A有子类C，所有返回C的列表
    print(C.__subclasses__())       #C没有子类，所以返回空列表

