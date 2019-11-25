from socket import *

csocket = socket(family=AF_INET,type=SOCK_STREAM)

ip = '127.0.0.1'
port = 15213
HOST = (ip,port)

csocket.connect(HOST)

while 1:
    msg = input('客户端发送消息：')
    csocket.send(msg.encode('utf-8'))
    if msg.lower() =="quit":                 #如果输入的是quit指令，退出循环
        break
    
    data = csocket.recv(1024).decode('utf-8') 
    print("客户端接收消息：",data)

    if data.lower() == "quit":
        break

csocket.close()