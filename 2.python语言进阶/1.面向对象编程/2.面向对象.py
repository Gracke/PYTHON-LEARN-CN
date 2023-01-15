"""
python实现面向对象的过程
"""
"""
1.定义类
"""
#编写了一个campus类，并在类中定义方法(函数)
class campus():
    # 初始化方法:初始化变量。绑定类属性，方便方法进行调用
    def __init__(self,name,college):
        self.name = name
        self.college = college
    def learn(self):
        print(f'恭喜{self.college}{self.name}同学获得奖学金')

"""
2.创建和使用对象
"""
class campus(): # 默认是objec,括号内可以你不填
    # 初始化方法:初始化变量。绑定类属性，方便方法进行调用
    def __init__(self,college,name):    # # name,age为局部变量,也是方法的参数
        self.name = name    # 将局部变量的值赋予给实例属性name
        self.college = college  #   将局部变量的值赋予给实例属性collage
    def scholarship(self):
        print(f'恭喜{self.college},{self.name}同学获得奖学金')

if __name__ == '__main__':
    stu1 = campus("计算机系","张三") # 创建类对象stu1
    stu2 = campus("管理系", "郑五")  # 创建类对象stu2
    stu1.scholarship()    # 使用对象stu1，调用方法scholarship()
    stu2.scholarship()    # 使用对像stu2，调用方法scholarship()

"""
动态绑定属性和方法
"""
class campus():
    student = '三好学生'
    def __init__(self,xm,age):
        self.name = xm
        self.age = age

    def show(self):
        print(f'我的名字:{self.name},年龄:{self.age}岁了')

if __name__ == '__main__':
    stu1 = campus('张三',20)
    stu2 = campus('李四',21)
    stu3 = campus('王五',22)
    print(stu1.name,stu1.age,)
    print(stu2.name,stu2.age)
    print(stu3.name,stu3.age)
    # 为动态绑定实例属性
    stu3.gender = '男'
    print(stu3.name,stu3.age,stu3.gender)
    # 动态绑定方法
    def introdunce():
        print('我是一个普通的函数，我被动态绑定为stu2的方法')
    # fun是命名的campus类内的方法，introdunce为普通函数
    stu2.fun= introdunce     #带括号叫方法调用，不带括号叫方法绑定
    stu2.fun()