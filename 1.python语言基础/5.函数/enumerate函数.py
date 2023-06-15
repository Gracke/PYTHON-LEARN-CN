"""
enumerate() 函数:
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    同时列出数据和数据下标，一般用在 for 循环当中。
"""
# 普通的 for 循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

print('----------------enumerate------------------------')

"""
for 循环使用 enumerate
"""
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)
