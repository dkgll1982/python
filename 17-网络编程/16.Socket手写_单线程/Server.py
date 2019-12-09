from socket import *
import time

#实例化对象
serversock = socket(family=AF_INET,type=SOCK_STREAM)

ip =''
port = 15213
HOST = (ip,port)

#绑定IP、端口
serversock.bind(HOST)

#监听客户端连接
serversock.listen(5) 
print('等待客户端连接...')

#阻塞直到有客户端连接进来
tcpclisock,addr = serversock.accept()
print(addr,'连接上服务器...',sep='')

#单线程程序也只会响应一个连接
while 1: 
    data = tcpclisock.recv(1024).decode('utf-8')
    if data is not None:
        print('服务端接收消息:',data)

    if data == "quit":                  #如果输入的是quit指令，退出循环
        break
    
    msg = input('服务端发送消息：')
    tcpclisock.send(msg.encode('utf-8')) 

    if msg.lower() =="quit":
        break

tcpclisock.close()
serversock.close()