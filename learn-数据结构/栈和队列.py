"""
栈: 一种数据集合,只能在一端进行插入与删除的操作
        push 进栈 li.append
        pop 出栈  li.pop
        get top 取栈顶 li[-1]
"""
class stack():
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

# stack = stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.pop()

"""栈-括号的匹配问题"""
class Stack():
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        self.stack.pop()
    def get_top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

def kuohao(str):
    match = {')':'(',']':'[','}':'{'}
    stack = Stack()
    for k in str:
        if k in {'(','[','{'}:
            stack.push(k)
        else:
            if stack.is_empty():    # data里只有右括号
                return False
            elif stack.get_top() == match[k]:
                stack.pop()
            else:                   # 栈顶与match 不匹配
                return False
    if stack.is_empty():        # 栈若空，则匹配完毕
        return True
    else:
        return False

print(kuohao('[({[([({})])]})]'))



"""
队列:一种数据容器,只允许在一端进行插入,另一端进行删除
实现:环型队列
"""
class Queue:
    def __init__(self,size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0
    def push(self,element):
        if not self.fill():
            self. rear = (self.rear + 1) % self.size
            self. queue[self.rear] = element
        else:
            raise IndexError('队列是空的')
    def pop(self):
        if not self.is_empty():
            self.front = (front.front +1) % self.size
            return queue[self.front]    # 通过被rear覆盖而出队列
        else:
            raise IndexError('队列是满的')
    def is_empty(self):
        return self.rear == self.front
    def fill(self):
        return (self.rear + 1) % self .size == self.front

q = Queue(5)
for i in range(2):
    q.push(i)

"""
双向队列:两端可以出队入队
"""
from collections import deque
# 单向队列
# d1 =deque([1,2,3,4,5],5)  # 第二个参数5为队列的长度,若队列满，则出队一个
# d1.append(6)
# print(d1.popleft())

# 双向队列
# d2 = deque([1,2,3,4,5],10)
# d2.appendleft()
# print(d2.pop())

def tail(n):
    with open('text','r',encoding='utf-8') as f:
        q = deque(f,n)
        return q

for line in tail(5):
    print(line,end='')

"""
迷宫问题:
    栈-深度优先搜索：回溯法
"""
