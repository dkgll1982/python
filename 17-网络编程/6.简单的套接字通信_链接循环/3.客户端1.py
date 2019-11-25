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
    phone.send(msg.encode('utf-8'))     #注意：不能发送空消息，否则服务器recive没有反应，比如input直接回车就是空消息

    data = phone.recv(1024)
    print("服务端回消息:",data.decode('utf-8'))

#4：挂电话
phone.close()