from socket import *

csocket = socket(family=AF_INET,type=SOCK_STREAM)

ip = '127.0.0.1'
port = 15213
HOST = (ip,port)

csocket.connect(HOST)

while 1:
    try:
        msg = input('客户端发送消息：')
        csocket.send(msg.encode('utf-8'))

        data = csocket.recv(4096).decode('utf-8')
        print("客户端接收消息：",data)
    except:
        print(HOST,'服务器已关闭\r\n')
        break