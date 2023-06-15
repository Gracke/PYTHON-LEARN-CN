"""
链表
"""
# class Node(object):
#     def __init__(self,item):
#         self.item = item
#         self.next = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# print(a.next.item)

print('-------------------------------------------------------')
"""头插法"""
class Node():       #建立一个空链表
    def __init__(self,items,next=None):
        self.item = items
        self.next = next

def create(data):
    head = Node(data[0])        # 建立一个头结点
    for element in data[1:]:    # 元素在头结点之后
        node = Node(element)    # 建立一个新结点
        node.next = head        # 新结点指向头结点（头插法）
        head = node             # 新结点成为新的头结点
    return head                 # 返回头结点

data=[1,2,3,4,5]
print(create(data).next.next.next.next.item)

print('-------------------------------------------------------')

"""尾插法"""
class Node:
    def __init__(self,items):
        self.item = items
        self.next = None

def tail(data):
    head = Node(data[0])        # 建立一个头结点
    tail = head                 # 头结点等于尾结点
    for element in data[1:]:    # 创建元素
        node = Node(element)    # 建立一个新的结点
        tail.next = node        # 尾结点指向新结点
        node = tail
    return head

data=[1,2,3,4,5]
print(create(data).next.next.next.next.item)

print('-------------------------------------------------------')


class Node():
    def __init__(self,item):
        self.item = item
        self.next = next

def head(data):
    head = Node(data[0])
    for element in data[1:]:
        node = Noda(element)
        node.next = head
        head = node
    return head

def insert(data):
    p = Node()
    p.next = curNode.next
    curNode.next = p
    return data

print('-------------------------------------------------------')

class RecordNode:
    def __init__(self,key,data):
        self.key = key
        self.data =data
class Sqlist():
    def __init__(self,MaxSize):
        self.MaxSize = MaxSize
        self.list =[None] * self.MaxSize
        self.len = 0
    def display(self):
        for i in range(self.len):
            print(self.list[i].key,end='')

    def insert(self,i,x):
        for j in range(self.len-1,i,-1):
            self.list[j] = self.list[j-1]
        self.list[i] = x
        self.len +=1

    def bubbling_sort(self):
        flag = True
        i = 1
        while i < self.len and flag:
            flag = False
            for j in range(self.len - i):
                if self.list[j + 1].key < self.list[j].key:
                    p = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = p
                    flag = True
                    list.display()
            i += 1

    def show(self):
        print('排序后的结果为:')
        self.bubbling_sort()

list = Sqlist(10)
data = [10,20,40,50,60,30]
for i,x in zip(range(len(data)),data):
    list.insert(i,RecordNode(x,x))
list.display()

