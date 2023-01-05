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
        # print(self.name)
        # self.show()

    # 静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性与实例方法')

stu1 = campus('张三',20)
stu2 = campus('李四',21)
stu3 = campus('王五',22)
print(stu1.name,stu1.age)
print(stu2.name,stu2.age)
print(stu3.name,stu3.age)

# 为动态绑定实例属性
stu3.gender = '男'
print(stu3.name,stu3.age,stu3.gender)

# 动态绑定方法
def introdunce():
    print('我是一个普通的函数，我被动态绑定为stu2的方法')

#fun是命名的campus类内的方法，introdunce为普通函数
stu2.fun= introdunce     #带括号叫方法调用，不带括号叫方法绑定
stu2.fun()