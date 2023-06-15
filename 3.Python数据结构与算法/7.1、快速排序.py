"""
快速排序
"""

"""使用递归对数组[2,4,6]进行求和"""


def sum(arr: list):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])


def count(arr: list):
    if not arr:
        return 0
    else:
        return len(arr)


def max(arr: list):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = max(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max


arr = [2, 4, 6]
print(sum(arr))
print(count(arr))
print(max(arr))

"""使用递归实现快速排列"""
import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # 使用随机化选择枢纽元素
        # pivot = random.choice(arr)
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


data = [9, 4, 6, 1, 7, 8, 2, 3, 5]
print(quicksort(data))

"""
使用循环实现快速排序
"""


def quick_sort(array):
    stack = [(0, len(array) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = array[left]
        i, j = left, right
        while i < j:
            while i < j and array[j] > pivot:
                j -= 1
            array[i] = array[j]
            while i < j and array[i] <= pivot:
                i += 1
            array[j] = array[i]
        array[i] = pivot
        stack.append((left, i - 1))
        stack.append((i + 1, right))
    return array


"""使用循环实现快速排序"""


def quick(data, left, right):  # 定义排序列表
    tmp = data[left]  # 储存拿出来的值进行左右划分
    while left < right:  # 防止两下标因为重合，而终止循环
        while left < right and data[right] >= tmp:  # 防止两下标因为重合
            right -= 1  # right的下标向左移动一个位置
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1  # left的下标向右移动一个位置
        data[right] = data[left]
    data[left] = tmp  # 将拿出来的数再储存一次，进行下次循环
    return left  # 返回left值


def sort(data, left, right):  # 定义分类列表的方法架构
    if left < right:  # 为将序列划分为两个区域而设置的判断条件
        mid = quick(data, left, right)  # 将拿出来的数作为中间值
        sort(data, mid + 1, right)  # 划分右边的区域
        sort(data, left, mid - 1)  # 划分左边的区域
    return data  # 返回 data值

