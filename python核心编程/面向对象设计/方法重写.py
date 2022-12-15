"""
方法重写：当父类的某个方法已不在适合子类，就需要在子类中重写父类的方法
"""
class campus():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我是{self.name}，我的年龄是{self.age}')

class student(campus):
    def __init__(self,name,age,stuno):
        super().__init__(name,age)           # 继承父类的name，age
        self.stuno = stuno
    def show(self):
        super().show()                      # 继承父类的show方法
        print(f'我的学号是{self.stuno}')


class teacher(campus):
    def __init__(self,name,age,department):
        campus.__init__(self,name,age)  # 继承父类的name，age
        self.department = department    # 赋予department的新变量
    def show(self):                     # 赋予teacher类的新方法
        print(f'我的姓名是{self.name}，年龄是{self.age}我的科室是{self.department}')


if __name__ == '__main__':
    r1 = student('李二',18,20220101)       # 子类student的对象名
    r2 = teacher('张大',25,'1-022')        # 子类teacher的对象名
    r1.show()
    r2.show()


"""object类-元类"""
class student(object):
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def show(self):
        print(f'名字:{self.name},年龄:{self.age}')
    # 重写__str__的方法
    def __str__(self):
        return '这是一个人,有name与age两个实例属性'


if __name__ == '__main__':
    stu = student('张三',18)
    print('---------------------------------------')
    # 返回结果一致
    print(stu)                #返回 <__main__.student object at 0x00000249310BBC70>
    print(stu.__str__())      #返回 <__main__.student object at 0x00000249310BBC70>
    print('---------------------------------------')
    # 当程序重写__str__方法时
    print(stu.__str__())      #返回 这是一个人,有name与age两个实例属性
    print(dir(stu.__str__()))
    # dir方法,返回一致
    print(stu.__dir__())
    print(dir(stu))


