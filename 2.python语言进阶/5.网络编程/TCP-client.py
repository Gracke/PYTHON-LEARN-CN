"""tcp-模拟客户端"""
import socket

#创建会话对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#创建链接对象
client.connect(('192.168.0.105',8001))

while True:
    data = input('请输入服务器信息')
    client.send(data.encode('utf-8'))   # 传输信息，并解码
    back_info = client.recv(1024).decode('utf-8')
    print('收到服务器信息:',back_info)