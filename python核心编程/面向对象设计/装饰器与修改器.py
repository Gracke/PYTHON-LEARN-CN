"""
@property可以直接用方法的名字调用，不用加括号
"""

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    #访问器-getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    #修改器 - setter方法
    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age <= 16:
            print(f'{self._name}正在玩飞行棋')
        else:
            print(f'{self._name}正在玩斗地主')

def main():
    person = Person('王五',36)
    person.play()
    person.age=22
    person.play()
    person.name



if __name__ == '__main__':
    main()


