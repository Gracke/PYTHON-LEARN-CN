"""
进程：操作系统执行中执行的一个程序，操作系统以进程为单位分配储存空间，
    每个进程都有自己的地址空间，数据栈以及用于跟踪进程执行的辅助数据，
    操作系统管理所有的进程的执行，为它们合理的分配资源
"""
# 单进程运行代码
from multiprocessing import  Process
import os
import time
"""
创建进程的方式:
    1.用于Unix,Linux,Mac的操作系统:os.fork()
    2.使用模块multiprocessing-process(group,target,name,kwargs)
    3.进程池-pool
"""
#主进程要等待所有子进程结束才能结束
def test():
    print(f'我的子进程的pid是{os.getpid()},我的父进程是{os.getppid()}')
    time.sleep(1)
if __name__ == '__main__':
    list = []
    print('主进程的执行开始')
    for i in range(5):
        #创建一个子进程对象
        pro=Process(target=test)
        pro.start()
        list.append(pro)
    for item in list:
        item.join()    #阻塞主进程
    print('主进程执行结束')    #只是主进程没代码了，才输出此行代码

"""
Proces的常用方法：
        name：当前进程实例别名，默认为Process-N
        pid：当前对象的pid值
        is_alive()：进程是否执行完，没执行完结果为True，否则为False
        join(sec)：等待结束或等待sec秒结束
        start()： 启动进程
        run()：如果没有指定target参数，则启动进程后，会调用父类的run方法
        terminate() 强制终止进程
"""
#多个进程同时执行的时候，执行顺序是随机的。
# def test_process1(name):
#     print(f'子进程的pid值是{os.getpid()},父进程的pid值是{os.getppid()}-------{name}')
#     time.sleep(1)
# def test_process2(age):
#     print(f'子进程的pid值是{os.getpid()},父进程的pid值是{os.getppid()}--------{age}')
#     time.sleep(1)
# if __name__ == '__main__':
#     print('主进程执行开始')
#     for i in range(5):
#         p1=Process(target=test_process1,args=('梅西',))   #无 target参数时，自动调用run()方法
#         p2=Process(target=test_process2,args=(35,))     #无 target参数时，自动调用run()方法
#         p1.start()
#         p2.start()
        # p1.terminate()    # 强制结束程序
        # p2.terminate()    # 强制结束程序
        # p1.run()      # 也可以主动调用
        # p2.run()      # 也可以主动调用t
        # p1.join()     # 等待P1子程序执行完后才执行下一条程序
        # p2.join()     # 等待p2子进程执行完后才执行下一条程序
        # print(p1.name,'是否执行完毕',p1.is_alive())
        # print(p2.name,'是否执行完毕',p2.is_alive())
        # print(p1.name,'的pid值:',p1.pid)
        # print(p1.name,'的pid值:',p2.pid)
    # print('主进程执行结束')

"""使用process类创建进程"""
# class test_process(Process):
#     def __init__(self,name):
#         Process.__init__(self)
#         self.name = name
#
#     def run(self):
#         print(f'进程名为{self.name},子进程的pid是{os.getpid()},父进程的pid是{os.getppid()}')
#
# if __name__ == '__main__':
#     print('进程执行开始')
#     for i in range(1,6):
#         p1 = test_process(f'process{i}')
#         p1.start()
#     print('进程结束')

"""
进程池语法结构: p = Pool(N)    N为最大进程个数
    apply_async(func,args,kwags)    使用非阻塞方式调用函数func
    apply(func,args,kwargs)     使用阻塞方式调用函数func
    close()     关闭进程池
    terminate()     终止进程
    join()      阻塞主进程，本必须在terminate或close之后使用
"""
from multiprocessing import Pool
import os
import time
def test(age):
    print(f'进程的名字:{age},子进程的pid值是{os.getpid()},父进程的pid值是{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('进程开始执行')
    # 创建一个进程池
    p = Pool(3)     # 设置最大进程数为3
    for i in range(10):
        # p.apply_async(func=test,args=(f'里奥·梅西第{i}次射门',))      #非阻塞性方式运行
        p.apply(func=test,args=(f'里奥·梅西第{i}次射门',))  #阻塞方式运行
    p.close()
    p.join()
    print('进程执行结束')