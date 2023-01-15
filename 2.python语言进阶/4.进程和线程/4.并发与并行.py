"""
并发:两个或多个进程同一时间间隔发生，多个进程被轮换着执行
并行:两个或多个进程在同一时刻发生，多条命令在同一时刻在多个处理器上同时执行
"""
# 全局变量的a在父进程与两子进程中各一份，各自操作自己全局变量的a的值，对与a的计算结果并没有在进程中传递，进程间没有共享数据
from multiprocessing import Process
a=100
def add():
    print('add进程执行开始')
    global a
    a += 30
    print('a=',a)
    print('add进程执行结束')
def sub():
    print('sub进程开始执行')
    global a
    a -= 30
    print('a=',a)
    print('sub进程执行介绍说')

if __name__ == '__main__':
    print('主进程开始执行')
    print('a=',a)
    p1 = Process(target=add)
    p2 = Process(target=sub)
    p1.start()
    p2.start()
