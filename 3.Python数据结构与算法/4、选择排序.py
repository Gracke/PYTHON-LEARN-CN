"""
选择排序
"""


def FindSmallest(data):  # 寻找最小值索引
    smallest = data[0]
    smallest_index = 0
    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
            smallest_index = i
    return smallest_index


def SelctionSort(data):  # 对数组进行排序
    newData = []
    for i in range(len(data)):
        smallest = FindSmallest(data)
        newData.append(data.pop(smallest))
    return newData


data = [5, 3, 6, 1, 2, 4, 7, 8]

print(SelctionSort(data))
