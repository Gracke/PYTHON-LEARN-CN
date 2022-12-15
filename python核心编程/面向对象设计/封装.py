class campus():
    def __init__(self,name,age,gender):
        self._name = name       #只有类与子类可以访问
        self.__age = age
        self.gender = gender

    def _func1(self):
        print('只有子类和类本身可以访问')       #对象可以访问

    def __func2(self):
        print('只有定义该方法的类的本身可以访问')       #对象不可访问，可以通过 对象名.类名__xxx进行访问

    #在类的普通实例方法内，在类的外部可以用'对象名'进行访问
    #在类的内部，使用'self'进行访问
    def show(self):
        self._func1()       # 类本身访问受保护的方法
        self.__func2()      # 类本身访问私有的方法
        print(self._name)   # 类本身访问保护的实例属性
        print(self.__age)   # 类本身访问私有的实例属性
        print(self.gender)  # 默认属性，可以随意访问


#建立对象名
if __name__ == '__main__' :
    #建立campus类型的对象stu
    stu = campus('张三',18,'男')
    print(stu._name)
    # print(stu.__age)   #报错，不能访问私用的方法
    stu._func1()
    # stu.__func2()     #报错，不能访问私用的方法
    stu.show()

print('---------------------------------------')

"""
调用私密方法
"""
class phone:
    def __init__(self,voltage):
        self.voltage = voltage

    def __keep_single_core(self):
        print('让cpu单核模式运行')

    def call_by_5g(self):
        if self.voltage >= 5:
            print('5G通话已开始')
        elif self.__keep_single_core():
            print('电量不足，已无法启用5G模式，已设置为单核模式进行省电')

if __name__ == '__main__':
    p =phone(10)
    p.call_by_5g()

print('---------------------------------------')

"""
excirxe
"""
class phone():
    def __init__(self,bool):
        self.__is_5g_enable = bool

    def __check_5g(self):
        if self.__is_5g_enable == True:     #类内
            print('5G开启')
        elif self.__is_5g_enable == False:
            print('5G关闭,使用4G网络')
    def call_by_5g(self):
            self.__check_5g()       #类内建立新方法调用私密方法
            print('正在通话中')

if __name__ == '__main__':
    light = phone(False)
    light.call_by_5g()






