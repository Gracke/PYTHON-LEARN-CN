"""
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

class Midea_AC(AC):
    def cool_wing(self):
        print('美的核心制冷')
    def hot_wind(self):
        print('美的电热丝加热')
    def swing_wind(self):
        print('美的无风感左右摆风')
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
