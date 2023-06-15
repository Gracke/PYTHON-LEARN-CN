def binary_search(data, val):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == val:
            return mid
        elif data[mid] > val:
            right = mid - 1
        else:
            left = mid + 1


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(data, 5))
