"""
变量注解:
    语法：变量名:注解
"""
#变量
var1 : int = 100
var2 : float = 3,1412
var3 : bool = True

#类对象
class student:
        pass

stu: student =student()

#容器类型
my_list : list =[1,2,3]
my_tuple : tuple = (1,2,3)
my_set : set = {1,2,3}
my_dict: dict = {'number':111}
#容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple: tuple[str,int,bool] = (1,2,3)
my_dict: dict[str,int] = {'11':11}
my_set: set[int] = {1,2,3,4}

"""
函数(方法)注解:
        语法：形参名:注解
用于注解返回值的注解:
        语法：def xxx() -> 注解
"""

def add(x:int,y:int):
        return x + y

#返回值的注解
def fun(data:list) -> list:
        return data
"""
Union类型注解
"""
from typing import Union
my_list: list[Union[str,int]] = [1, 2,'grack']
my_dict: dict[Union[str,str],Union[str,int]]= {'name':'zzz','age':11}

def func(data:Union[int,str]) -> int:
        pass