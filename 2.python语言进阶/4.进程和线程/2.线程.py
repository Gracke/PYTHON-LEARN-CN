"""
多任务的方式:
    一个应用程序内使用多个进程
    一个进程内使用多个线程
线程：
    cpu可调度的最小单位
    被包含在进程中，是进程中实际的运作单位
    一个进程中可以并发多个线程，每条线程并行执行不同的任务
"""
import threading

"""
创建线程的方式:
    1.使用threading模块创建线程
    2.使用函数式创建线程
        t= Thread(gruop,target,name,args,kwargs)
    3.使用 Thread子类创建线程
"""
#函数式创建
from threading import Thread
import time
#
# def test():
#     time.sleep(1)
#     for i in range(3):
#         print(f'线程{threading.current_thread().name},执行{i}次')   # 线程几执行几次
#
# if __name__ == '__main__':
#     start = time.time()
#     print('主线程开始执行')
#     list = []
#     for i in range(2):
#         t = Thread(target=test)
#         t.start()
#         list.append(t)
#     for item in list:
#         item.join()
#
#     print('主线程开始执行')
#     end = time.time()
#     print(f'时间耗时{end - start}')

#继承 Thread子类创建进程
class sub_t(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'线程{threading.current_thread().name},执行{i}次')


if __name__ == '__main__':
    print('主线程开始执行')
    list =[sub_t() for _ in range(2)]
    for item in list:
        item.start()
    for item in list:
        item.join()