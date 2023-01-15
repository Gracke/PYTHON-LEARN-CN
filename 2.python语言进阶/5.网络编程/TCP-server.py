"""tcp-模拟服务器"""
import socket

#创建会话对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立链接(服务器进行连接时，需要一直在线,所有不能用一次链接connect)
server.bind(('192.168.0.105',8001))

#设置监听,5相当于线程数
server.listen(3)    #传输信息的个数

#阻塞链接(等待链接)
info,addr = server.accept()

#等待数据
while True:
    data = info.recv(1024)
    print('收到客户端信息:', data.decode('utf-8'))
    send_data = input('请返回数据给客户端:')
    info.send(send_data.encode('utf-8'))

