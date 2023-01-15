"""
使用队列实现生产者模式与消费者模式:
    Queue
"""
from queue import Queue     # 实现线程
from threading import Thread
import time
class producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue = queue

    def run(self):
        for i in range(1,6):
            print(f'进程{self.name},放入元素{i}')
            self.queue.put(i)
            time.sleep(1)
        print('生产者已存入所有的数据')

class consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue = queue

    def run(self):
        for i in range(1,6):
            item = self.queue.get()
            print(f'进程{self.name}已出队{item}')
            time.sleep(1)
        print('消费者已取出所有的数据')

if __name__ == '__main__':
    print('模式开始执行')
    queue = Queue()
    p = producer('produnce',queue)
    c = consumer('counsume',queue)
    p.start()
    c.start()
    p.join()
    c.join()
