"""
迷宫问题:
    栈-深度优先搜索：回溯法
"""
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def map_path(x1,y1,x2,y2):      #竖代表x轴，横代表y轴
    direction = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1)
    ]
    stack = []
    stack.append((x1,y1))   # 添加的不是一个单一的值,而是一个整体(坐标)
    while len(stack) > 0 :
        curNode = stack[-1]     #现在的栈顶就是当前的坐标
        # map[x1][x2] = 2
        if curNode[0] == x2 and curNode[1] == y2:
            for i in stack:
                print(i)
            return True
        for dir in direction:
            nextNode = dir(curNode[0],curNode[1])      # dir()是diretion内其中的一个lambda方法，pi
            if map[nextNode[0]][nextNode[1]] == 0:  # 用map检索坐标
                stack.append(nextNode)
                map[nextNode[0]][nextNode[1]] = 2
                break
        else:
            # map[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('没路了')
        return False


map_path(1,1,8,8)

"""
迷宫问题:
    队列-广度优先搜索
"""
