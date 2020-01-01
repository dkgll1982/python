# 基于gevent的并发服务器实现
import gevent
# 将python内置的socket换成封装了IO多路复用的socket
from gevent import monkey
# 导gevent中的猴子补丁，来把原来python自带的socket变成基于epoll的socket（解除阻塞问题）
monkey.patch_all()
import socket

# 封装了epoll的套接字，可避开阻塞
server = socket.socket()
# 绑定ip和端口
server.bind(('0.0.0.0', 8000))
# 绑定监听数量  
server.listen(1000)

def worker(*args):
    connection, addr = args  
    """
    协程需要处理的事情
    :param connection:
    :return:
    """
    while True:
        try:
            print("Client {0} connected".format(addr))
            recv_data = connection.recv(1024)  # 等待接收数据
            if recv_data:
                print(addr,recv_data.decode('gbk'))
                # 将接收的数据原路返回
                connection.send(recv_data) 
            else:
                # 发送完毕断开
                connection.close()  
                break
        except ConnectionResetError:
            print("Client {0} disconnected".format(addr))
            break

while True:
    # 等待客户端连接，遇到阻塞切换
    conn, addr = server.accept()  
    # 生成协程，并将conn作为参数传入
    gevent.spawn(worker,conn,addr)  