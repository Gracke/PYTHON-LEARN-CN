"""闭包:将全局变量的安全度增加，因为全局变量有被修改的风险"""
def outer(logo):
    def func(msg):
        return f'{logo} is {msg}'
    return func     # 闭包一定要返回方法名
if __name__ == '__main__':
    t1 = outer('未来维度')
    print(t1('great'))

"""使用nonlocal改变外部方法变量"""
def outer(num1):
    def inter(num2):
         nonlocal num1
         num1 += num2
         return num1
    return inter
if __name__ == '__main__':
    t2 = outer(10)
    print(t2(5))
    print(t2(5))
    print(t2(5))

"""闭包实现ATM"""
def count(amount=0):
    def ATM(num,deposit=True):
        nonlocal amount
        if deposit:
            amount += num
            return f'存入+{num}元，现有余额:{amount}'
        else:
            amount -= num
            return f'取出-{num}元,现有余额:{amount}'
    return ATM

c = count()
print(c(100))
print(c(100))
print(c(120))
print(c(10,False))