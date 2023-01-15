#打开(创建)文件
def my_write():
    file =open('new.txt','w',encoding='utf-8')  #‘w’为覆盖写模式
    # 文件写入
    file.write('伟大的中国梦')
    # 文件关闭
    file.close()

# 读文件
def my_read():
    # 打开文件
    file = open('new.txt','r+',encoding='utf-8')
    # 文件读出
    print(file.read())

"""
文件的打开方式:
        r 以只读模式打开，文件若不存在，则error
        rb 以只读文件打开二进制文件
        w 覆盖写模式,文件存在则覆盖，文件不在则创建
        wb 文件录入二进制文件,文件存在则覆盖，文件不在则录入
        a 追加写模式,文件不存在创建,文件存在,则在文件最后追加内容
        + 与w/r/a同时使用，（既可以读又可以写）
文件的读写方法:
        file.read(size) 读取文件中的size个字节或字符，默认读取全部
        file.readline(size) 读取文件中的一行的size个数据,默认则为读取这一行中的全部
        file.readlines() 从文件中的读取所有内容,结果为列表类型
        file.write() 写入数值
        file.writelines(lst) 将内容全部为字符串的列表lst写入文件
        flie.seek(offset) 改变当前的文件操作指针位置,英文占一个字节，中文gbk编码占两个字节,utf-8编码占三个字节

"""
def pattern (str):
    file = open('new.txt','a',encoding='utf-8')
    file.write(str)
    file.write('\n')
    file.close()

# pattern('我的中国梦')
# pattern('我的中国心')

def write_list (file,lst):
    file = open(file,'a',encoding='utf-8')
    file.writelines(lst)
    file.close()

# lst= ['姓名','年龄','性别\n','z\t','z\t','z']
# file = 'new1.txt'
# write_list(file,lst)

def read_txt(file):
    file = open(file,'w+',encoding='utf-8')
    file.write('不知道')
    file.seek(3)
    s=file.read()
    print(s)

read_txt('new.txt')

"""
文件的复制
"""
def copy(t1,t2):
    # 打开各自的文件
    file1=open(t1,'r',encoding='utf-8')
    file2=open(t2,'w',encoding='utf-8')
    # 复制操作
    s=file1.read()      # 读文件1
    file2.write(s)      # 将文件1的内容复制到第二个
    # 关闭文件
    file2.close()
    file1.close()


# copy('new.txt','new1.txt')

"""
with语句:处理文件时，无论是否右异常，都能保证with语句执行后关闭打开的文件
        with open(...)as file:
            pass
"""
def write ():
    with open('new.txt','w',encoding='utf-8') as file:
        file.write('2022卡塔尔世界杯')

def read():
    with open('new.txt','r',encoding='utf-8') as file:
        r = file.read()
        print(r)
write()
read()

