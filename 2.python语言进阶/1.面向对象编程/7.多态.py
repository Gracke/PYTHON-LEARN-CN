"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
多态：不关心是否有相同的数据类型与是否具有继承关系(平行关系)，只关心是否存在同名方法
"""
class person():
    def eat(self):
        print('人吃五谷杂粮')

class cat():
    def eat(self):
        print('猫喜欢吃鱼')

class dog():
    def eat(self):
        print('狗喜欢吃骨头')

def fun(obj):
    obj.eat()

if __name__ == '__main__':
    per = person()
    cat = cat()
    dog = dog()
    # 调用函数
    fun(per)
    fun(cat)
    fun(dog)

print('----------------------------------')

"""
抽象类：含有抽象方法的类
    方体体为空实现的(pass)的称为抽象方法
"""
class AC:
    def cool_wing(self):
        '制冷系统'
        pass
    def hot_wind(self):
        '制热系统'
        pass
    def swing_wind(self):
        '左右摆风系统'
        pass
"""美的空调"""
class Midea_AC(AC):
    def cool_wing(self):
        print('美的核心制冷')
    def hot_wind(self):
        print('美的电热丝加热')
    def swing_wind(self):
        print('美的无风感左右摆风')
"""格力空调"""
class GREE_AC(AC):
    def cool_wing(self):
        print('格力变频省电制冷')
    def hot_wind(self):
        print('格力电热丝加热')
    def swing_wind(self):
        print('格力静音左右摆风')

def device(ac):
    ac.cool_wing()
    ac.hot_wind()
    ac.swing_wind()

if __name__ == '__main__':
    mi = Midea_AC()
    ge = GREE_AC()
    device(mi)

print('----------------------------------')

# 抽象类的另一个实例
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod # 抽象方法
    # 所在的 class Pet 继承 abc.ABCMeata
    # 给需要抽象的实例方法添加装饰器 @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()