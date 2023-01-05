"""
继承
"""
class campus():     #campus是父类
    def __init__(self,name,age):        # 初始化方法
        self.name = name
        self.age = age

    def show(self):         # 定义方法
        print(f'我是{self.name}，我的年龄是{self.age}')

class student(campus):      # campus的子类-stundent类
    def __init__(self,name,age,stuno):
        super().__init__(name,age)      # super().继承campus类的name，age实例变量
        self.stuno = stuno


class teacher(campus):      # campus的子类-teacher类
    def __init__(self,name,age,department):
        campus.__init__(self,name,age)  # campus.继承campus类的name，age实例变量
        self.department = department

if __name__ == '__main__':
    r1 = student('李二',18,20220101)
    r2 = teacher('张大',25,'1-022')
    r1.show()       # 用子类的对象调用父类的方法
    r2.show()       # #用子类的对象调用父类的方法

"""
多继承
"""
class FatherA():
    def __init__(self,name):
        self.name = name

    def showA(self):
        print('调用父类a的方法')

class FatherB():
    def __init__(self,age):
        self.age = age

    def showB(self):
        print('调用父类b的方法')

class son(FatherA,FatherB):     # 继承a与b两个父类
    def __init__(self,name,age,hobby):
        FatherA.__init__(self,name)     # 继承父类a的属性
        FatherB.__init__(self,age)      # 继承父类b的属性
        self.hobby = hobby          #赋予新的属性hobby

if __name__ == '__main__':
    s = son('张三',18,'乒乓球')

    #若没有方法，用pass跳过，也能调用父类的方法，因为子类已经继承
    s.showA()
    s.showB()