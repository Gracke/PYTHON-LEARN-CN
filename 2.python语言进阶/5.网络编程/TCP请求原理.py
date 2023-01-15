"""tcp通信:通过建立可靠的链接，通信双方都可以用数据流的方式发送数据"""
import socket

# 创建会话对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立链接
sk.connect(('www.pyqt5.cn',80))

#发送请求
sk.send(b'GET / HTTP/1.1\r\nHost: www.pyqt5.cn\r\nConnection: close\r\n\r\n')

#等待数据
list=[]
while True:
    re_data = sk.recv(1024)
    if re_data:
        list.append(re_data)
    else:
        break
list_str = (b''.join(list)).decode('utf-8')
print(list_str)
