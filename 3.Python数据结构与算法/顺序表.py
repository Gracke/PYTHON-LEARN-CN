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
            print(self.list[i].key,end=',')

    def insert(self,i,x):
        for j in range(self.len-1,i,-1):
            self.list[j] = self.list[j-1]
        self.list[i] = x
        self.len +=1
    def __bubbling_sort(self):
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
            i += 1

    def dichotomy(self,target):
        if self.len>0:
            left = 0
            right = self.len-1
            while left<=right:
                mid = int((left+right)/2)
                if self.list[mid].key==target:
                    return mid
                elif self.list[mid].key<target:
                    left = mid +1
                else:
                    right = mid -1
        return -1

    def show(self):
        self.__bubbling_sort()
        print('排序后的结果为:')
        list.display()
        print()
        print('查找出的值:')


list = Sqlist(100)
data = [157,171,156,178,151,156,163,160,165,158,181,189,168,157,179,150,161,154,178,158,177,169,170,156,173,179,167,171,182,174,167,157,173,168,188,152,177,186,158,183,177,171,162,157,178,164,175,170,152,162]
for i,x in zip(range(len(data)),data):
    list.insert(i,RecordNode(x,x))
list.show()
print(list.dichotomy(168))

