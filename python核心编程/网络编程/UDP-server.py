"""udp-客户端"""
import socket

#创建会话对象
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#建立链接(服务器进行连接时，需要一直在线,所有不能用一次链接connect)
server.bind(('192.168.0.105',8002))

while True:
    info,addr = server.recvfrom(1024)
    print('收到客户端信息:',info.decode('utf-8'))
    send_data =input('请返回数据给客户端：')
    server.sendto(send_data.enc1ode('utf-8'),addr)