"""
继承
1.在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
2.在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
"""
class Campus():
    """校园"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def stu_award(self):
        print('%s获得国家奖学金' % self._name)

    def te_award(self):
        print('%s获得优秀教师奖' % self._name)
class Student(Campus):
    def __init__(self,name,age,college):
        super().__init__(name, age)     # 通过upper()方法,继承父类属性
        self._college = college

    @property
    def college(self):
        return self._college
    @college.setter
    def college(self,college):
        self._college = college

    def study(self,course):
        print('%s的%s正在学习%s.' % (self._college, self._name, course))


class Teacher(Campus):
    """老师"""

    def __init__(self, name, age, title):
        Campus.__init__(self,name, age)     # 通过父类调用初始化方法
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '计算机系')    # 设置子类Student对象stu
    stu.study('数学')     # 子类对象调用子类方法
    stu.stu_award()     # 子类可以调用父类方法
    t = Teacher('Gracke', 38, '教授')     # 设置子类Teacher对象t
    t.teach('Python程序设计')
    t.te_award()    # 子类可以调用父类方法

if __name__ == '__main__':
    main()


"""
继承的另一种形式:
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


