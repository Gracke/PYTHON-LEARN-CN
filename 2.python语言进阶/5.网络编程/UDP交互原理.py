"""
UDP通信:
    以面向无连接的协议进行数据交互，只有ip和端口就可以以广播的形式发送
    因为数据传输都不建立可靠链接，UDP传输数据可靠性低，传输速度比tcp快很多
"""
import socket
udp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#因为udp是无连接的协议，所以不用建立链接，直接发送信息
data= input('输入的信息:')
udp.sendto(data,endcode('utf-8'),(xxx.xxx.x.x,8888))
