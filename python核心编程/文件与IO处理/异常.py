"""
异常捕获的基本语法:
        try:
            ··················
        except:
            ··················
"""
try:
    flie= open('D:/jamin/txt','r',encoding='utf-8')
except:
    print('程序出现bug，已捕获')
    #更改异常
    # flie = open('jamin.txt', 'w', encoding='utf-8')

print('------------------------------------------------------------------------')

"""
捕获指定异常:
        try:
            ··················
        except xxxx as 变量:        
"""
try:
    print(name)
except NameError as n : #n变量记录异常的信息数据
    print('NameError出现错误,name无定义')
    print(n)

print('------------------------------------------------------------------------')

"""
捕获多个异常:
        try:
            ·················
        except (xxxxxx,xxxxxxx) as 变量:
"""
try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print('程序出现异常')
    print(e)

print('------------------------------------------------------------------------')

"""
捕获多个异常:
        try:
            ·············
        except Exception as 变量:
"""
try:
    1 / 0
    print(hello)
    print(error)
    flie= open('D:/jamis/txt','r',encoding='utf-8')
    1/0
except Exception as r:
    print(r)

print('------------------------------------------------------------------------')

"""异常else"""
try:
    print('hello')
except:
    print('已经检测出异常')
else:
    print('检测出无异常')

print('------------------------------------------------------------------------')

"""
异常finally: 无论程序是否异常，我都要执行程序
"""
try:
    f = open('a.txt','r',encoding='utf-8')
except:
    print('程序异常')
else:
    print('程序无异常')
finally:
    f.close()

def func1 ():
    print('func1开始')
    1/0
    print('func2结束')
def func2():
    print('fuc开始')
    func1()
    print('fun2结束')

def main():
    try:
        func2()
    except Exception as e:
        print('func1异常')
        print(e)

main()
