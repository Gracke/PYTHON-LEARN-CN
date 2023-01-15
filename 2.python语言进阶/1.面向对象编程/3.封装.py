"""
面向对象有三大支柱：封装、继承和多态
这一节先讲封装,讲封装前需要了解访问可见性
"""

"""
访问可见性-保护与私有:
单下划线
"""
class Test:
    def __init__(self, name,phone):
        self._name = name
        self.__phone = phone
    def _func1(self):
        print('可以在外部和类直接调用')
        print('只有子类和类本身可以访问')
        print(self._name)
        print(self.__phone)
    def __func2(self):
        print('无法在外部和类直接调用')
        print('只有定义该方法的类的本身可以访问')
        print(self._name)
        print(self.__phone)
    def __pri(self):
        print("该方法为私有方法")
    def show(self):
        self.__func2()

def main():
    test = Test('张三',44152)
    test._func1()
    # test.__func2() 'Test' object has no attribute '__func()' 无法用类直接调用私密方法
    print(test._name)
    # print(test.__phone) 'Test' object has no attribute '__phone' 无法用类直接调用私密方法
    """调用私密方法"""
    # 1. 在类中定义公有方法，在方法内调用私有属性与私有方法
    test.show()
    print('---------------------------------')
    # 2.对象名调用保护类名(protect)再调用保护属性,方法是非法的，不建议使用
    print(test._Test__phone)
    # 3.对象名调用类名(protect)再调用保护属性,方法是非法的，不建议使用
    test._Test__pri()
if __name__ == "__main__":
    main()

"""
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。
这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻，关于这一点可以看看我的
"""

"""
封装的理解是"隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口"。
封装数据的主要原因是：保护隐私（把不想别人知道的东西封装起来），减少执行代码的复杂度和增加代码执行的有序性

我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，
在我们创建了对象之后，只需要给对象发送一个消息（调用方法）就可以执行方法中的代码，
也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节（方法的内部视图）。
提示：
    在编程语言里，对外提供的接口（接口可理解为了一个入口），就是函数，称为接口函数，这与接口的概念还不一样，接口代表一组接口函数的集合体。
"""

class phone():
    def __init__(self,bool):
        self.__is_5g_enable = bool

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print('5G开启')
        elif self.__is_5g_enable == False:
            print('5G关闭,使用4G网络')
    def call_by_5g(self):
            self.__check_5g()
            print('正在通话中')

if __name__ == '__main__':
    light = phone(False)
    light.call_by_5g()

