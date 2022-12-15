class Circle():
    def __init__(self,r):
        self.r =r

    def get_area(self):
        return 3.14*self.r**2
    def get_perimeter(self):
        return 2*3.14*self.r


if __name__ == '__main__':
    cir = Circle(eval(input('请输入圆的半径：')))
    print(f'圆的面积为:{cir.get_area()}')
    print(f'圆的周长为:{cir.get_perimeter()}')


# class student():
#     def __init__(self,name,age,adress):
#             self.name = name
#             self.age = age
#             self.adress = adress
#
#     def show(self):
#         print(self.name,self.age,self.adress)


class  instrument():
    def make_sound(self):
        pass

class erhu(instrument):
    def make_sound(self):
        print('二胡在弹奏')

class piano(instrument):
    def make_sound(self):
        print('钢琴在弹奏')

class violin(instrument):
    def make_sound(self):
        print('小提琴在弹奏')

def play(obj):
    obj.make_sound()

if __name__ == '__main__':
    e = erhu()
    p = piano()
    v = violin()
    play(e)
    play(p)
    play(v)


"""excirxe"""
# class student():
#     def __init__(self,name,age,adress):
#             self.name = name
#             self.age = age
#             self.adress = adress
#             print(f'学生{i}信息录入成功,信息为【学生年龄:{self.name},年龄:{self.age},地址:{self.adress}】')
#
#     def show(self):
#         print(f'学生年龄:{self.name},年龄:{self.age},地址:{self.adress}')
# if __name__ == '__main__':
#     list = []
#     for i in range(1,4):
#         print(f'当前录入第{i}位，总共有10位学生信息')
#         stu = student(input('请输入学生信息：'),input('请输入学生年龄：'),input('请输入学生地址：'))
#         list.append(stu)
# #将输入的学生数据打印出来
#     for item in list:
#         item.show()

