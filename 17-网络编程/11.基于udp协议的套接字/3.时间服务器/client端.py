#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from socket import *
ip_port=('127.0.0.1',9000)
bufsize=1024

tcp_client=socket(AF_INET,SOCK_DGRAM)



while True:
    msg=input('请输入时间格式(例%Y %m %d)>>: ').strip()
    tcp_client.sendto(msg.encode('utf-8'),ip_port)

    data=tcp_client.recvfrom(bufsize)

    print(data.decode('utf-8'))

tcp_client.close() 