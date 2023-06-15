"""
数组：
    是一种数据结构，内存地址是连续的，每个地址储存的一个数据，每个地址都是已知的，可以进行随机访问
    当执行读取操作时，可以直接对地址进行访问，运行时间：O(1)
    当进行插入操作时，需将后面的数据往后移动一格，运行时间：O(N)
    当进行删除操作时，需将前面的数据往前移动一格,运行时间：O(N)

"""


class MyArray:
    """
    A simple wrapper around List.
    You cannot have -1 in the array.
    """

    # 初始化
    def __init__(self, capacity: int):
        # 创建空列表，存储数据
        self._data = []
        # 限定数组容量
        self._capacity = capacity

    # 获取列表中的元素
    def __getitem__(self, position: int) -> object:
        return self._data[position]

    # 设置列表中的元素
    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    # 获取列表的长度
    def __len__(self) -> int:
        return len(self._data)

    # 迭代器，用于循环遍历列表中的元素
    def __iter__(self):
        for item in self._data:
            yield item

    # 查找数组中的元素
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    # 删除数组中的元素
    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    # 插入元素到数组指定位置
    def insert(self, index: int, value: int) -> bool:
        # 判断数组长度是否超出限制
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    # 打印数组中的所有元素
    def print_all(self):
        for item in self:
            print(item)


# 测试MyArray类的各个方法
def test_array():
    # 创建一个容量为5的MyArray对象
    array = MyArray(5)
    # 在数组的第0个位置插入元素3
    array.insert(0, 3)
    # 在数组的第0个位置插入元素4
    array.insert(0, 4)
    # 在数组的第1个位置插入元素5
    array.insert(1, 5)
    # 在数组的第3个位置插入元素9
    array.insert(3, 9)
    # 在数组的第3个位置插入元素10
    array.insert(3, 10)
    # 插入元素100失败，因为数组已满
    assert array.insert(0, 100) is False
    # 验证数组长度为5
    assert len(array) == 5
    # 验证数组第1个位置的元素为5
    assert array.find(1) == 5
    # 删除数组的第4个位置的元素
    assert array.delete(4) is True
    # 打印数组中的所有元素
    array.print_all()


if __name__ == '__main__':
    test_array()

"""
yield 是 Python 中的一个关键字，用于定义生成器函数，
它的作用是将函数的执行过程挂起，返回一个中间结果给调用方，然后在需要的时候恢复执行过程，直到函数执行完毕或者遇到了 return 语句。

try 是 Python 中的异常处理机制，用于检测程序中的错误，并在错误发生时进行相应的处理。
try 语句块中包含可能会引发异常的代码，而 except 语句块则包含了对这些异常的处理方法。

assert 是一个断言语句，用于判断条件表达式是否为 True，如果不为 True 则会引发 AssertionError 异常。
一般在代码中使用 assert 可以用来做代码调试，可以在关键的代码段加入断言语句，以保证代码的正确性。
如果运行程序时某个断言不成立，那么会引发异常，进而终止程序的运行。
"""

"""
    1) Insertion, deletion and search of singly-linked list;
    2) Assumes int type for data in list nodes.

    Author: Wenru
"""
