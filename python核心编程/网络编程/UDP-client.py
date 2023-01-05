import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    data = input('输入服务器的信息')
    client.sendto(data.encode('utf-8'),('192.168.0.105',8002))
    back_info = client.recvfrom(1024)
    print('接收的信息是',back_info[0].decode('utf-8'))