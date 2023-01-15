"""
设计模式:是一种编程思路，可以极大的方便程序的开发
    1.单例模式
    2.工厂模式
"""

"""
单例模式:对一个类，只获取其类中唯一的实例对象，持续复用它
    ·节省内存
    ·节省多次创建对象的浪费
"""
# 创建一个test1的模块
from test1 import tool_str

#两个变量共用一个实例对象
t1 = tool_str
t2 = tool_str
print(t1)   #<test1.ToolStr object at 0x00000183C0BC7B80>
print(t2)   #<test1.ToolStr object at 0x00000183C0BC7B80>

"""
工厂模式:有统一的入口，易维护
"""
class Person:
    pass

class Woker(Person):
    pass
class Administrator(Person):
    pass
class CEO(Person):
    pass

class Factory:
    def get_people(self,p_type):
        if p_type == 'w':
            return Woker()
        elif p_type == 'a':
            return Administrator()
        elif p_type == 'c':
            return CEO()

if __name__ == '__main__':
    f = Factory()
    worker =f.get_people('w')
    admin =f.get_people('a')
    ceo = f.get_people('c')