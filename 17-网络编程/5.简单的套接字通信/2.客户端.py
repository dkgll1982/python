import socket

#1：买手机
phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

#2：拨号
phone.connect(('127.0.0.1',8080))

#3：发、收消息
while True:
    msg = input('客户端发消息->').strip()
    if not msg:
        continue
    #注意：不能发送空消息，否则服务器recive没有反应，比如input直接回车就是空消息
    #原因：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，
    #     而udp是基于数据报的，即便是你输入的是空内容（直接回车），那也不是空消息，udp协议会帮你封装上消息头
    phone.send(msg.encode('utf-8'))     

    data = phone.recv(1024)
    print("服务端回消息:",data.decode('utf-8'))

#4：挂电话
phone.close()