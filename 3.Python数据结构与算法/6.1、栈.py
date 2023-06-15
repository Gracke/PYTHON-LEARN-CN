"""
调用栈的简单实现
"""


def greet(name):
    print("hello," + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print("how are you," + name + "?")


def bye():
    print("ok bye!")


greet("Jamin")

"""
当你调用greet("Jamin"),计算机将首先为该函数发调用分配一块内存。
我们使用内存时。变量name是设置为Jamin，这需要储存到内存中。
每当你调用函数时，计算机都像这样将函数调用涉及的所有变量的值存储到内存中。接下来，你打印hello，jamin！，再调用"greet2("Jamin")。
同样，计算机也为该函数调用分配一块内存。
---------------------------------
计算机使用一个栈来表示这些内存块，其中第二个内存块位于第一个内存块上面。
打印出how are you,Jamin?，然后从函数调用返回。此时，栈顶的内存块被弹出。
现在栈顶的内传存块是函数greet的，这意味这你返回到了函数greet。
当你调用到函数greet时，函数只执行类一部分，该函数的所有变量值都在内存中。执行完函数greet2后，你回到函数greet。
之后再打印getting ready to say bye...，再调用函数bye，再栈顶添加bye的内存块。然后，你打印ok bye！并从这个函数返回。
现在你又回到函数greet，由于无事可做，函数greet就返回了。这个栈用于存储多个函数的变量，被调用栈。
"""

"""递归调用栈"""


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))

"""
栈虽然很方便，但是在存储详细的信息可能会占用大量的内存。
每一次调用一次函数都要占用一定的内存，如果栈很高时，就意味着计算机存储的大量的函数调用信息。
你有两种方式解决这种情况-大量内存占用
    1.重新编写代码，使用循环
    2.使用尾递归
"""


