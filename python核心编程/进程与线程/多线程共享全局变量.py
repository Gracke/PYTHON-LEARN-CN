"""多线程下,全局变量是共享的"""
import threading
from threading import Thread
import time
# a = 100
# def add():
#     global a
#     print('开始执行')
#     a += 30
#     print(f'执行结果:{a}')
#
# def sub():
#     time.sleep(1)
#     global a
#     print('开始执行')
#     a -= 60
#     print(f'执行结果:{a}')
#
# if __name__ == '__main__':
#     print('线程开始执行')
#     t1 = Thread(target=add)
#     t2 = Thread(target=sub)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('线程结束执行')


"""
线程共享的安全性:由于线程的同时进行，可能会发生数据错乱的
"""
# from threading import Thread
# import time
#
# ticket = 50
# def ticket_sell():
#     global ticket
#     for i in range(1000):
#         if ticket > 0:
#             ticket -= 1
#             print(f'正在出售第{ticket}张票{threading.current_thread().name}')
#
# if __name__ == '__main__':
#     print('开始售票')
#     for i in range(3):
#         t = Thread(target=ticket_sell)
#         t.start()
#
#     print('售票结束')

"""
互斥锁：
-创建锁对象
lock_obj =Lock()
-lock类的方法
上锁:lock_obj.acquire()
解锁:lock_obj.release()
"""
from threading import Thread,Lock
import threading
import time

ticket = 50
lock_obj = Lock()
def ticket_sell():
    global ticket
    for i in range(1000):
        lock_obj.acquire()
        if ticket > 0:
            print(f'{threading.current_thread().name}出售第{ticket}张票')
            ticket -= 1
        time.sleep(1)
        lock_obj.release()
if __name__ == '__main__':
    print('开始售票')
    for i in range(3):
        t = Thread(target=ticket_sell)
        t.start()
    print('售票结束')




