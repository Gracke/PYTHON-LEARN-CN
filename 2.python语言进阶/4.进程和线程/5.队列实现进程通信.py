"""
运用队列来实现进程之间的通信： q=Queue(N) N为可通信的个数
        qsize() 获取当前队列包含的消息数量
        empty() 判断队列是否为空,为空结果为True,否则为False
        full() 判断队列是否满了,满为True，否则为False
        get(block=True) 获取队列中的一条信息，然后从队列中移除,block默认为True
        get_nowait() 相当于get(block=False),当消息队列为空时,抛出异常
        put(item,block=True) 将item消息放入队列,block默认为True
        put_nowait(item) 相当于put(item,block=False)
"""
from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    print('判断队列是否为空',q.empty())
    print('判断队列是否为满',q.full())
    q.put('阿根廷')
    q.put('梅西')
    print('队列的消息为',q.qsize())
    print('判断队列是否为空',q.empty())
    print('判断队列是否为满',q.full())
    q.put(35)
    print('队列的消息为', q.qsize())
    print('判断队列是否为空', q.empty())
    print('判断队列是否为满', q.full())
    # q.put('大力神杯',timeout=3)       #当消息队列满时,放入消息为堵塞进程,会等待出队才停止进程,timeout可以设置等待的时间
    # q.put_nowait('大力神杯',)   #当消息队列满的时候，直接报错，不会等待消息的出队
    # q.get()         #若队本身是空的，则会等待队列的进队，才出队，否则进程一直运行
    # q.get(block=False) # 若信息队列中为空时，则会直接报错，不会等待
    print('队列的消息为', q.qsize())
    print('判断队列是否为空', q.empty())
    print('判断队列是否为满', q.full())
    # 遍历出队列中所有的元素
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())

"""队列实现进程通信"""
from multiprocessing import Process
from multiprocessing import Queue
import time
a = 1000
def write_put(q):
    global a
    if not q.full():
        for i in range(10):
            a -= 10
            q.put(a)
            print('入队的值',a)

def read_get(q):
    time.sleep(1)
    global a
    while not q.empty():
        print('读取的值',q.get())


if __name__ == '__main__':
    print('主程序开始执行')
    q = Queue()
    p1 = Process(target=write_put,args=(q,))
    p2 = Process(target=read_get,args=(q,))
    p1.start()
    p2.start()
    print('主程序结束执行')
    p1.join()
    p2.join()