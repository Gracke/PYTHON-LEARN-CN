"""
模块的导入: import xxx
"""
# # import xxx
# import time
# print('你好')
# time.sleep(5)       #执行此行代码时，程序休眠5秒钟
# print('在吗')

# from xxx import xxx
# from time import sleep
# print('你好')
# sleep(3)
# print('再见')

# from xxx import * 所有功能导入
# from time import *
# print('你好')
# sleep(3)
# print('再见')

"""
as定义别名:
    import xxx as xx
    from xxx import xx as x
"""
# # import time as t
# # print('a')
# # t.sleep(3)
# # print('b')
# from time import sleep as t
# print('a')
# t(3)
# print('b')

"""自定义模块"""
# import add
# add.test(1,2)

# 不同摸模块的同名功能
# from add import test
# from subtract import test     # 模块二的功能把模块一给覆盖了，只执行模块二的功能
# test(9,1)

# 模块的测试

# if __name__ == '__main__':     #模块内的测试,不会影响模块的使用

# __all__=['方法名

"""
python包:文件夹下包含一个__init__.py的文件,改文件夹包含多个模块包
"""
# 使用包
# import package.模块名
#
# __all__=['模块名'] 写在__init__中
