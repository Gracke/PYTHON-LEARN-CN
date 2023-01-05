"""
类-class
对象
"""
#编写了一个campus类
class campus():
    pass
#编写了一个student类
class student():
    pass

#类的对象
cam = campus()      # per为person类型的对象
stu = student()     # c就为cat类型的对象
print(type(cam))    # 返回 <class '__main__.campus'>
print(type(stu))    # 返回 <class '__main__.campus'>

print('==========================================================')

"""
类的组成
"""
class campus():
    student = '三好学生'      #为类属性，定义在类里面，被所有对象所共享
    #初始化方法__init__(创建不同的实例属性进行实例方法)
    def __init__(self,xm,age):      # name,age为局部变量,也是方法的参数
        self.name = xm      # 将局部变量的值赋予给实例属性self.name
        self.age = age      # 实例属性的名称与局部变量的名称相同而已，还是两种不同的属性

    # 实例方法
    def show(self):
        print(f'我的名字:{self.name},年龄:{self.age}岁了')    #格式化内的值为实例属性

    # 类方法
    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性与实例方法')


    # 静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性与实例方法')


"""类的组成部分的使用"""
cam = campus('asd',18)
# 对象名打点实例属性，输出默认参数
print(cam.name,cam.age)

# 对象名访问类属性
print(campus.student)

# 使用对象名调用实例方法
cam.show()
campus.show(cam)

# 使用类名调用类方法
campus.cm()

# 使用类名调用静态方法
campus.sm()
#实例属性不能通过类访问

print('==========================================================')

"""创建对象"""
# 属性值相同，属性名不同
#类属性被所有对象共享
stu1 = campus('asd',18)
stu2 = campus('梅西',20)
stu3 = campus('123',19)
print(type(stu1))
print(type(stu2))
print(type(stu3))
print('--------------------------------------------------------')
#修改类属性的值
campus.student ='优秀党员'
print(stu1.name,stu1.age)
print('--------------------------------------------------------')
#将对象放到组合数据类型存储。存储到列表中
list = [stu1,stu2,stu3]
for element in list:        # element的数据类型为campus，element是一个campus类的对象
    element.show()

print('--------------------------------------------------------')

"""
@classmethod:在类中定义类方法
"""
class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)  #cls被成为方法中的方法
        cls().func1()  # 调用 func1 方法


A.func2()
print('--------------------------------------------------------')
"""
@staticmethod:静态方法,不用通过设置变量来调用方法
"""
class C(object):
    @staticmethod
    def f():
        print('runoob');

# C.f();  # 静态方法无需实例化
# b = C()
# b.f()  # 也可以实例化后调用
C.f()