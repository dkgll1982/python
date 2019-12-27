# 基于gevent的并发服务器实现
import gevent
# 将python内置的socket换成封装了IO多路复用的socket
from  gevent import monkey;monkey.patch_all()
import socket

# 实例化socket
server = socket.socket()
# 绑定ip和端口
server.bind(('0.0.0.0', 8000))
# 绑定监听数量
server.listen(1000)

def worker(connection):
    """
    协程需要处理的事情
    :param connection:
    :return:
    """
    while True:
        recv_data = connection.recv(1024)  # 等待接收数据
        if recv_data:
            print(recv_data)
            connection.send(recv_data)  # 将接收的数据原路返回
        else:
            connection.close()  # 发送完毕断开
            break

while True:
    conn, addr = server.accept()  # 等待客户端连接，遇到阻塞切换
    gevent.spawn(worker, conn)  # 生成协程，并将conn作为参数传入