"""
装饰器:创建闭包函数，用闭包函数调用目标函数
"""
# def sleep():
#     import time
#     import random
#     r = random.randint(1, 10)
#     time.sleep(r)
#
# def outer(func):
#     def inner():
#         print('我要睡觉了')
#         func()
#         print('我睡醒了')
#     return inner
#
# if __name__ == '__main__':
#     f = outer(sleep)
#     f()

"""@方法名"""
def outer(func):
    def inner():
        print('我要睡觉了')
        func()
    return inner
@outer
def sleep():
    import time
    import random
    r = random.randint(1, 10)
    time.sleep(r)
    print(f'我睡醒了，睡了{r}秒')

if __name__ == '__main__':
    sleep()