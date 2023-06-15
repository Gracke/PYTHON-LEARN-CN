"""
    Stack based upon linked list
    基于链表实现的栈

    Author: Wenru
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next


class LinkedStack:
    def __init__(self):
        self._top: Node = None

    def clear(self):
        self._top = None

    def is_empty(self) -> bool:
        return self._top is None

    def length(self):
        l = 0
        p = self._top
        while p is not None:
            p = p._next
            l += 1
        return l

    def push(self, value: int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value
        else:
            return None

    # 重载repr函数，用于打印栈中元素
    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(str(current._data))
            current = current._next
        return "[" + " -> ".join(nums) + "]"
        # nums = [str(current._data) for current in self if current]
        #   return "[" + " -> ".join(nums) + "]"

    def __len__(self) -> int:
        return self.length()


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)