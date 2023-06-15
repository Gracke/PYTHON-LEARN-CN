"""顺序表实现快速排序（三路快排）"""
import random


class RecordNode:
    def __init__(self, key, data):
        self.key = key  # 节点的关键字
        self.data = data  # 节点的数据


class SqList:
    def __init__(self, maxSize):
        self.maxSize = maxSize  # 顺序表的最大长度
        self.list = [None] * maxSize  # 初始化顺序表为一个元素为None的列表
        self.len = 0  # 顺序表的长度为0

    def insert(self, i, x):
        if self.len == self.maxSize:
            raise Exception("顺序表已满")
        if i < 0 or i > self.len:
            raise Exception("插入位置不合理")
        for j in range(self.len - 1, i, -1):
            self.list[j] = self.list[j - 1]
        self.list[i] = x
        self.len += 1

    def partition(self, low, high):
        pivot = self.list[random.randint(low, high)]  # 随机选择一个枢轴元素
        lt, gt, i = low - 1, high + 1, low  # lt、gt初始化为low-1和high+1，i初始化为low
        while i < gt:  # 只要i小于gt就继续循环
            if self.list[i] < pivot:  # 如果当前元素小于枢轴元素
                lt += 1  # lt加1
                self.list[lt], self.list[i] = self.list[i], self.list[lt]  # 交换lt和i位置上的元素
                i += 1  # i加1
            elif self.list[i] > pivot:  # 如果当前元素大于枢轴元素
                gt -= 1  # gt减1
                self.list[gt], self.list[i] = self.list[i], self.list[gt]  # 交换gt和i位置上的元素
            else:  # 如果当前元素等于枢轴元素
                i += 1  # i加1
        self.list[low:high + 1] = self.list[lt + 1:gt]  # 将枢轴元素放在中间，返回枢轴元素的位置
        return lt + 1

    def quick_sort(self, low, high):
        if low < high:  # 如果low小于high
            p = self.partition(low, high)  # 进行一趟划分操作，将列表分为两部分
            self.quick_sort(low, p - 1)  # 递归对左半部分进行快速排序
            self.quick_sort(p + 1, high)  # 递归对右半部分进行快速排序

    def display(self):
        for i in range(self.len):
            print(self.list[i].key, end=',')

    def show(self):
        self.quick_sort(0, len(self.list) - 1)
        print('排序后的结果为:')
        list.display()
        print()
        print('查找出的值:')


if __name__ == '__main__':
    list = SqList(10)
    data = [10, 20, 40, 100, 50, 60, 30, 90]
    for i, x in zip(range(len(data)), data):
        list.insert(i, RecordNode(x, x))
    list.display()
