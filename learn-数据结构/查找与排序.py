"""
顺序查找
"""
#way-one
# def search (data,object):       # data是数据容器，object是目标对象
#     for i in range(len(data)):  # len(data)是容器的长度，嵌套个range()就遍历出每个元素的下标
#         if data[i] == object:   # i 就是找出目标函数的下标
#             return i            # 若找到该元素，则返回
#     return                      # 否则，返回None

# way-another
# def seek (data,target):                     # data是数据容器，target是目标对象
#     for index,str in enumerate(data):       #index是下标，str是下标对应字符
#         if str == target:
#             return index
#         else:
#             return None
print('-------------------------------------------------------------------------------')
"""
二分查找
"""
# def dichotomy (data,target):
#     left = 0
#     right = len(data)-1
#     while left <= right:
#         mid = (left+right) // 2      # mid是取中间值的下标，mid的变量就是为了取中间值
#         if data[mid] == target:      # 若data[mid]已经取到目标元素target，则返回mid
#             return mid
#         elif data[mid] > target:    #若检索到data[mid]>大于目标函数target，则right往mid前面移动一格
#             right = mid - 1
#         else :                      #若检索到data[mid]都不满足以上条件，则一定小于目标函数target，所以left往mid的后面移动一格
#             left = mid + 1
#
# data = [1,2,3,4,5,6,7,8,9]
# print(dichotomy(data,8))

print('-------------------------------------------------------------------------------')

"""
冒泡排序
"""
def bubbling (data):
    for i in range(len(data)-1):        #从第0次开始，循环i次(i=0,...,len(data)-1-1)
        for j in range(len(data)-i-1):  #设置下标位置
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data

data = [1,5,7,3,8,4,2,6,10,9]
print(bubbling(data))

print('-------------------------------------------------------------------------------')

"""
选择排序
"""
# def select (data):
#     for i in range(len(data)-1):        # 循环i次，i=(0,1,2,3)
#         min = i     # 设置最小值,此为序列中的第一个数
#         for j in range(i+1,len(data)):  # 给每个循环设置下标
#             if data[min] > data[j]:
#                 min = j     # 更换最小值，重复for语句循环
#         data[i],data[min] = data[min],data[i]   #新的最小值的位置与原来最小值的位置为2上
#     return data
#

# def select (data):
#     for i in range(len(data)-1):            # 循环i次，i=(0,1,2,3)
#         for j in range(i+1,len(data)):      # 给每个循环设置下标
#             min = i                         # 设置最小值
#             if data[min] > data[j]:         # 目前的最小值大于检索值
#                 min = j                     # 更换最小值，重复for语句循环
#             data[i],data[min] = data[min],data[i]
#     return data
#
# data =[3,5,4,2,13,1,6,12,9,8,7,10,11]
# print(select(data))

print('-------------------------------------------------------------------------------')

"""
插入排序
"""
def list_insert (data):
    for i in range(1,len(data)):     # 摸牌的下标
        tmp = data[i]           # 储存自己摸到的牌，防止因为移动被覆盖掉
        j = i-1                 # 设置手里第一张牌的下标
        while j >= 0 and data[j] > tmp :
            data[j+1] =data[j]     #将手中的最右的牌(每次循环中的第一张)向右移动一个位置
            j -= 1          # 将摸到的牌按顺序放到手牌中
        data[j+1] =tmp      # 储存自己手中的被移动的牌
    return data

data = [8,1,7,2,3,5,6,4]
print(list_insert(data))

"""
快速排序
"""
def quick (data,left,right):        # 定义排序列表
    tmp = data[left]        # 储存拿出来的值进行左右划分
    while left < right:     # 防止两下标因为重合，而终止循环
        while left < right and data[right] >= tmp:   # 防止两下标因为重合
            right -= 1      # right的下标向左移动一个位置
        data[left] = data[right] 
        while left < right and data[left] <= tmp:
            left += 1       # left的下标向右移动一个位置
        data[right] = data[left]
    data[left] = tmp        # 将拿出来的数再储存一次，进行下次循环
    return left             # 返回left值

def  sort (data,left,right):    # 定义分类列表的方法架构
    if left < right:        # 为将序列划分为两个区域而设置的判断条件
        mid = quick(data,left,right)    # 将拿出来的数作为中间值
        sort(data,mid+1,right)          # 划分右边的区域
        sort(data,left,mid-1)           # 划分左边的区域
    return data                         # 返回 data值
data = [5,7,1,3,6,9,10,4,2,8]
print(sort(data,0,len(data)-1))         # 设置相应的默认参数

