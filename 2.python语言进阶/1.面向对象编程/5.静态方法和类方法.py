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

C.f()
# 静态方法无需实例化
# b = C()
# b.f()  # 也可以实例化后调用
