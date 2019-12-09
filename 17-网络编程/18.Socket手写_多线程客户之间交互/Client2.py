from socket import *

csocket  = socket(family=AF_INET,type=SOCK_STREAM)

ip = '127.0.0.1'
port = 15243
HOST = (ip,port)
user = '用户2'
friend = '用户1'

csocket.connect(HOST)
csocket.send(user.encode('utf-8'))       #发送用户名

while 1:
    try:
        msg = input(user+':') 
        if not msg:
            continue

        #发送好友消息（此处示例注意：发送的内容分两部分，用":"分隔，前边为好友用户名，后边为内容）
        sendStr = friend + ":" + msg
        csocket.send(sendStr.encode('utf-8'))

        data = csocket.recv(4096).decode('utf-8')
        print(data)
    except:
        print(HOST,'服务器已关闭\r\n')
        break